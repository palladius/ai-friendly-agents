
# 1. global imports
from google.adk.agents import Agent
from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.readonly_context import ReadonlyContext
import logging
import dotenv
import os
from typing import List, Dict, Any, Tuple, Optional, Type
import datetime
import platform


########################################################
# BEGIN Carlessian needed magical lines to import lib/ (God didn't write the world in Python, I tell you that! Perl or Ruby, but not Python).
# See `agents/README.md` for more info.
#
# --- MAGIC PATH FIXING START ---
import os, sys # if needed
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
sys.path.insert(0, project_root)
# --- MAGIC PATH FIXING END ---
########################################################

# 2. local imports
from lib.sqlite_agent import * # SQLiteAgent, print_database_schema
from lib.colors import Color

########################################
# ENV part - with dotenv of course.
dotenv.load_dotenv()

# --- Configuration ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#DEFAULT_DB_FILE = 'siculo/my_test_db.sqlite'
DEFAULT_DB_FILE = 'agents/siculo/google_events.sqlite'
#DEFAULT_DB_FILE = 'siculo/google_events.sqlite'


sample_questions = [
    'Whats the name and path of the DB?',
    'Show me a nice-looking schema dump of the DB',
    # depends on DB, but could be:
    'When is the next event? Show me the value AND the sql query you used, in backticks.',
]

def getenv_boolean(var_name: str, default: bool = False) -> bool:
    '''
    Helper function to get a boolean value from an environment variable.
    '''
    value = os.getenv(var_name, str(default)).lower()
    if value in ['true', '1', 'yes']:
        return True
    elif value in ['false', '0', 'no']:
        return False
    else:
        raise ValueError(f"Invalid boolean value for {var_name}: {value}")

# ENV -> vars
DB_FILE = os.getenv("SICULO_AGENT_DB_FILE", DEFAULT_DB_FILE)
# https://stackoverflow.com/questions/63116419/evaluate-boolean-environment-variable-in-python
#ALLOW_WRITES = os.getenv("SICULO_AGENT_ALLOW_WRITES", False)
#DEBUG = os.getenv("SICULO_AGENT_DEBUG", False)
ALLOW_WRITES = getenv_boolean("SICULO_AGENT_ALLOW_WRITES", False)
DEBUG = getenv_boolean("SICULO_AGENT_DEBUG", False)
RAILS_ROOT = os.getenv("RAILS_ROOT", os.path.dirname(os.path.realpath(__file__)))

print(f">>> DB_FILE={DB_FILE}")
SingletonAgent = SQLiteAgent(filename=DB_FILE, write_access=ALLOW_WRITES, debug=DEBUG)

# -- Tool part --

def tool_get_database_details():
    '''
        Retrieves enhanced details for all tables, including schema and row counts.

        Returns:
            Dict[str, Any]: A dictionary containing 'db_filename' and 'table_details'.
                            'table_details' is a dict mapping table names to their
                            schema and row count ({'schema': {...}, 'rows': int}).
                            Row count is -1 if it cannot be determined.
    '''
    return SingletonAgent.get_database_details()

def tool_execute_sql(sql_query: str):
    '''Executes a generic SQL query on the DB.'''
    print(f"Executing query.. ```{sql_query}```") # todo color blue
    return SingletonAgent.execute_sql(sql_query)

# def tool_execute_natural_language_query(nl_query: str):
#     '''Executes a natural language query on the DB.'''
#     return SingletonAgent.execute_natural_language_query(nl_query)

def tool_list_tables():
    '''Lists all user-defined tables in the database.'''
    return SingletonAgent.list_tables()

def tool_get_table_schema(table_name: str):
    '''Retrieves the schema (column names and types) for a given table.'''
    return SingletonAgent.get_table_schema(table_name)

def tool_get_full_schema()-> Dict[str, Dict[str, str]]:
    '''Retrieves the schema for all tables in the database.'''
    return SingletonAgent.get_full_schema()

def tool_get_colorful_database_schema_markdown():
    '''Takes the enhanced database details and prints a colorful representation.'''
    database_details = SingletonAgent.get_database_details()
    # TODO wrap with try..
    ret = database_schema_to_colorful_markdown(database_details)
    return {
        "status": "success",
        "result": ret,
    }

    #return { "status": "success", "log": "Database schema printed to console. Sorry Gemini you cant see it but it was beautiful" }
# --- Agent ---

BASE_INSTRUCTION = (
    "You are Salvatore Siculo (nicknames 'Salvo' or 'Siculo'), a SQL expert."
    "You'll be able to look at DB structure and answer questions about it."
    "You will use tools to access schema, tables, and rows. You'll be able to execute generic SQL for one given multi-DB file."
    "Currently just supports sqlite3."
    ""
    "Whenever asked about date, time, location, version or context, feel free to call the `tool_simple_context` tool. Apart from that, all you do is SQL."
    "At the beginning, start greeting the user, introduce yourself, then use tools to access the database."
    "make yourself aware of the tables, a a relationship among tables, in order to be able to answer questions by the users"
)

async def preload_db_schema_callback(callback_context: CallbackContext):
    """
    A before_agent_callback that loads the DB schema into session state on the first turn.
    """
    if not callback_context.state.get("db_schema_loaded"):
        #logging.info("DB schema not loaded for session %s. Loading now.", callback_context.session_id)
        logging.info("DB schema not loaded for session %s. Loading now.", callback_context.state.get("session_id"))
        db_details = tool_get_database_details()
        schema_markdown = database_schema_to_colorful_markdown(db_details)

        callback_context.state['db_schema'] = schema_markdown
        callback_context.state["db_schema_loaded"] = True

    # Return None to allow the agent to continue its run.
    return None

def get_instruction_with_schema(ctx: ReadonlyContext) -> str:
    """
    An InstructionProvider that dynamically builds the instruction,
    prepending the DB schema if it's available in the session state.
    """
    #schema_markdown = ctx.session.state.get('db_schema')
    schema_markdown = ctx.state.get('db_schema')
    if schema_markdown:
        return f"DATABASE SCHEMA:\n{schema_markdown}\n\nINSTRUCTIONS:\n{BASE_INSTRUCTION}"
    return BASE_INSTRUCTION


def tool_simple_context():
    '''Returns info on the machine where the agent is running: date, path, some ENV vars, user location and software VERSION.'''
    # Read agent version from "./VERSION" file
    print()
    path_to_version_file = os.path.join(RAILS_ROOT, "VERSION")
    if not os.path.exists(path_to_version_file):
        agent_version = "VERSION file not found"
    else:
        with open(path_to_version_file, "r") as f:
            agent_version = f.read().strip()


    return {
        'date_today': datetime.datetime.today().strftime('%Y-%m-%d'),
        'time_now': datetime.datetime.now().strftime('%H:%M:%S'),
        'user_name': 'Salvatore Siculo',
        'user_location':  os.getenv('USER_LOCATION', 'Taormina, Sicily'),
        'ENV[FOO]': os.getenv('FOO', 'FOO not set'),
        'ENV[BAR]': os.getenv('BAR', 'BAR not set'),
        'ENV[DB_FILE]': os.getenv('DB_FILE', 'DB_FILE not set'),
        'ENV[ALLOW_WRITES]': os.getenv('ALLOW_WRITES', 'ALLOW_WRITES not set'),
        'ENV[DEBUG]': os.getenv('DEBUG', 'DEBUG not set'),
        'cwd': os.getcwd(),
        'os_name': platform.system(),
        'agent_version': agent_version,
    }


root_agent = Agent(
   name="salvatore_siculo__sql_agent", # Salvatore "SQL" Siculo
   model="gemini-2.0-flash", # might not be enough.. but doesnt support BIDI
   # Maube gemini-2.5-pro-preview-05-06 ? Nope
   #model="gemini-2.5-pro-preview-05-06", # works with BIDI, but not with websockets
#   model="gemini-2.5-pro", # websockets.exceptions.ConnectionClosedError: received 1008 (policy violation) models/gemini-2.5-pro is not found for API version v1alpha, or is not supported for bidiGenerateContent. Call ListModels to; then sent 1008 (policy violation) models/gemini-2.5-pro is not found for API version v1alpha, or is not supported for bidiGenerateContent. Call ListModels to
   description="Agent to answer questions on SQL databases. ",
   # Instructions to set the agent's behavior.
   instruction=get_instruction_with_schema,
   before_agent_callback=preload_db_schema_callback,
   tools=[
       tool_get_database_details,
       tool_execute_sql,
       tool_list_tables,
       tool_get_table_schema,
       tool_get_full_schema,
       #tool_print_database_schema,
       tool_get_colorful_database_schema_markdown,
       tool_simple_context,
       ],
)


if __name__ == "__main__":
    print("-- rough testing of agent tool calling --")
#     print(tool_print_database_schema())
    print(tool_simple_context())
