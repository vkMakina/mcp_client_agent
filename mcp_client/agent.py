import asyncio
from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, SseServerParams

# Function to get MCP tools asynchronously
async def get_mcp_tools():
    """Get tools from the MCP server."""
    tools, exit_stack = await MCPToolset.from_server(
        connection_params=SseServerParams(
            url="http://localhost:8001/sse"
        )
    )
    return tools

# Get the tools synchronously for agent initialization
# This is a workaround for the async/sync mismatch in ADK
try:
    # Try to get the current event loop
    loop = asyncio.get_running_loop()
    # If there's already a running loop, we need to use a different approach
    import nest_asyncio
    nest_asyncio.apply()
    mcp_tools = asyncio.run(get_mcp_tools())
except RuntimeError:
    # No running loop, safe to create a new one
    mcp_tools = asyncio.run(get_mcp_tools())

# Create the agent with the retrieved MCP tools
agent = LlmAgent(
    name="mcp_agent",
    model="gemini-2.0-flash-lite",
    description="Agent with MCP tools",
    instruction="""
    You are a helpful assistant that can use the tools provided by the MCP server.
    """,
    tools=mcp_tools
)

# ADK requires a root_agent attribute for web server integration
root_agent = agent
