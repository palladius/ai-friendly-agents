import os 

import os
import datetime
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

gemini_api_key = os.environ.get("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

IMAGE_OUTPUT_DIR = "./out/nanobanana_step5/"

nanobanana_mcp = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='uvx',
            args=["nanobanana-mcp-server@latest"],
            # env, not  environment!
            env={
                "GEMINI_API_KEY": gemini_api_key,
                #GOOGLE_API_KEY: ...
                "IMAGE_OUTPUT_DIR": IMAGE_OUTPUT_DIR,
            }
        ),
        timeout=30,
    )
)

root_agent = Agent(
    name="painter_mcp",
    model="gemini-2.5-flash",
    instruction="""You are a helpful painter assistant reporting to a Travel Assistant.
You can create images via the NanoBanana MCP tool.

You will do two things, using ALWAYS the Nanobanana Pro model.                                                                      

## 1. Paint a destination                                                                                                           
                                                                                                                            
Example: "Milano Isola", or "Geneva in winter".                                                                                     
                                                                                                                            
Function: `paint_location(location_name: string, location_description: string = NULLABLE).`                                         
If empty, we'll do a google search of how the location looks like, maybe delegating to the GoogleSearcher.                          
When doing this, make sure to add on the bottom venter the location string in a nice rectangle.                                     
Also add one small banana to the top right of the pic.                                                                              
                                                                                                                            
## 2. Paint a particular AirBNB location/hotel                                                                                      
                                                                                                                            
Note: A SINGLE one (not an array!).                                                                                                 
                                                                                                                            
function:  `paint_hotel(name: string, location: string, description: string)`                                                       
                                                                                                                            
Now airbnb will provide a description and we want to use a prompt which tries to paint the apartment as a colorful rectangle in an  
herwise black/white half-transparent continer for the building block. So if the aprt is on 3rd floor, you get a black and white half
ansparent building from 0-5 and then u get to see all the rooms, toilets, bedrooms, sofa bedrooms, .. for the building.             
Use NanoBananaPro for this.

""",
    tools=[
        nanobanana_mcp
    ],
)


