import os
import datetime
from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from google.adk.tools.tool_context import ToolContext
from google.genai import types

gemini_api_key = os.environ.get("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY environment variable not set.")

IMAGE_OUTPUT_DIR = "./nanobanana_step5/"

# TOOL 1: The original MCP Toolset to generate the image file
nanobanana_mcp = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command='uvx',
            args=["nanobanana-mcp-server@latest"],
            env={
                "GEMINI_API_KEY": gemini_api_key,
                "IMAGE_OUTPUT_DIR": IMAGE_OUTPUT_DIR,
            }
        ),
        # its timeout, not  timeout_in_seconds!
        timeout=60  # Increased timeout for image generation
    )
)

# TOOL 2: A new tool to read a local image file and display it in the chat
async def display_image(filename: str, tool_context: ToolContext):
    """Reads an image file from the local disk and displays it in the chat as an artifact."""
    
    # The nanobanana server provides a relative path, let's ensure it's correct
    # The IMAGE_OUTPUT_DIR is where the server saves the files.
    full_path = os.path.join(IMAGE_OUTPUT_DIR, os.path.basename(filename))

    try:
        with open(full_path, "rb") as f:
            image_bytes = f.read()
        
        await tool_context.save_artifact(
            os.path.basename(full_path),
            types.Part.from_bytes(data=image_bytes, mime_type='image/png'),
        )
        return {
            'status': 'success',
            'detail': f'Image "{os.path.basename(full_path)}" displayed successfully.',
        }
    except FileNotFoundError:
        return {"status": "failed", "detail": f"Image file not found at path: {full_path}"}
    except Exception as e:
        return {"status": "failed", "detail": f"An error occurred: {e}"}


root_agent = Agent(
    name="painter_mcp",
    model="gemini-2.5-flash",
    instruction="""You are a helpful painter assistant. You have two tools.

1.  `generate_image(prompt: str)`: Creates an image from a text prompt and saves it to a file. It returns the filename of the created image.
2.  `display_image(filename: str)`: Takes a filename and displays the image in the chat.

Your workflow is a two-step process:
- **Step 1:** Use the `generate_image` tool to create the image based on the user's request.
- **Step 2:** Take the `filename` provided in the output of `generate_image` and immediately call the `display_image` tool with that filename to show the result to the user.
""",
    tools=[
        nanobanana_mcp,
        display_image,
    ],
)
