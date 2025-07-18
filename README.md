# MCP Client Agent

A Model Context Protocol (MCP) client agent integrated with Google's Agent Development Kit (ADK).

## Overview

This project demonstrates how to create an AI agent that can connect to MCP servers and use their tools through the ADK framework. The agent can be deployed as a web service and interact with various MCP-compatible tools.

## Features

- **MCP Integration**: Connects to MCP servers via Server-Sent Events (SSE)
- **ADK Web Interface**: Provides a web UI for interacting with the agent
- **Async/Sync Compatibility**: Handles the async nature of MCP tools within ADK's sync requirements
- **Tool Integration**: Automatically loads and uses tools from connected MCP servers

## Project Structure

```
mcp_client_agent/
├── mcp_client/
│   ├── __init__.py
│   └── agent.py          # Main agent implementation
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not tracked)
└── README.md
```

## Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   - Ensure your MCP server is running (default: `http://localhost:8001/sse`)
   - Update the MCP server URL in `mcp_client/agent.py` if needed

3. **Run the Agent**:
   ```bash
   adk web --port 8002
   ```

## Configuration

The agent is configured in `mcp_client/agent.py`:

- **MCP Server URL**: Currently set to `http://localhost:8001/sse`
- **Model**: Uses `gemini-2.0-flash-lite`
- **Agent Name**: `mcp_agent`

## Technical Details

### Async/Sync Handling

The project uses `nest_asyncio` to handle the async nature of MCP tool loading within ADK's synchronous initialization:

```python
# Handles event loop conflicts
import nest_asyncio
nest_asyncio.apply()
mcp_tools = asyncio.run(get_mcp_tools())
```

### MCP Connection

Connects to MCP servers using Server-Sent Events:

```python
tools, exit_stack = await MCPToolset.from_server(
    connection_params=SseServerParams(
        url="http://localhost:8001/sse"
    )
)
```

## Usage

1. Start your MCP server on port 8001
2. Run the ADK web server: `adk web --port 8002`
3. Open `http://localhost:8002` in your browser
4. Interact with the agent through the web interface

## Dependencies

- `google-adk`: Agent Development Kit
- `nest_asyncio`: Async event loop handling
- Other dependencies as listed in `requirements.txt`

## Troubleshooting

- **Port Conflicts**: Ensure MCP server (8001) and ADK server (8002) use different ports
- **Event Loop Errors**: The `nest_asyncio` package should handle most async/sync conflicts
- **Connection Issues**: Verify your MCP server is running and accessible

## License

MIT License