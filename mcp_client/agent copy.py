from google.adk.agents import Agent
from google.adk.tools import google_search
from datetime import datetime

def get_current_time() -> dict:
    """
    Get the current time.
    """
    return {
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }

root_agent = Agent(
    name="tool_agent",
    model="gemini-2.0-flash-lite",
    description="Tool agent",
    instruction="""
    You are a helpful assistant that can use the tools
    """,
    tools=[get_current_time],
    # tools=[get_current_time],
    # tools=[google_search, get_current_time], # <--- Doesn't work
)
