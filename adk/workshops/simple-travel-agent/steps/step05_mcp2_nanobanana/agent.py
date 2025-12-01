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

IMAGE_OUTPUT_DIR = "./step05_mcp2_nanobanana/nanobanana_step5/"

# TOOL 1: The original MCP Toolset to generate the image file
# Note: this has a number of tools:
# 🟢 nanobanana (from nanobanana) - Ready (7 tools)
#   Tools:
#   - edit_image
#   - generate_diagram
#   - generate_icon
#   - generate_image
#   - generate_pattern
#   - generate_story
#   - restore_image

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
async def display_image_with_adk(filename: str, tool_context: ToolContext):
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
    instruction="""You are a helpful painter assistant. Your primary goal is to create and display images based on user requests.

**Your Workflow (Two Steps):**
1.  **`generate_image(prompt: str)`**: First, you MUST call this tool to create an image. The prompt you create for this tool will follow the detailed creative rules below. This tool returns the filename of the generated image.
2.  **`display_image_with_adk(filename: str)`**: Immediately after `generate_image` succeeds, you MUST call this tool, using the `filename` from the previous step's output to show the image to the user.

**Creative Rules for `generate_image` prompt:**
You will do two things, using ALWAYS the Nanobanana Pro model.

**1. Paint a destination**
   - **Example**: "Milano Isola", or "Geneva in winter".
   - **Function Logic**: `paint_location(location_name: str, location_description: str = NULLABLE)`.
   - **Details**:
     - If the description is empty, you might need to find information first (though you don't have a search tool right now).
     - When painting a destination, add the location string in a nice rectangle at the bottom center of the image.
     - Also add one small banana to the top right of the pic. 🍌
     - also ad a small blue rectangle on top left "Made with ADK", white over blue.

**2. Paint a particular AirBNB location/hotel**
   - **Note**: A SINGLE one (not an array!).
   - **Function Logic**: `paint_hotel(name: str, location: str, description: str)`.
   - **Details**:
     - Use the provided AirBNB description to paint the apartment as a colorful rectangle inside an otherwise black-and-white, semi-transparent container representing the building.
     - For example, if the apartment is on the 3rd floor of a 5-story building, you'd draw the semi-transparent building and then the detailed, colorful apartment on the 3rd floor, showing its rooms (toilets, bedrooms, etc.).
     - Use the NanoBanana Pro model for this.
""",
    tools=[
        nanobanana_mcp,
        display_image_with_adk,
    ],
)
