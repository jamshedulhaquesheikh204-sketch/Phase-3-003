"""MCP Server Runner

This script runs the MCP server standalone.
"""

from mcp_server import mcp
import asyncio

if __name__ == "__main__":
    # Run the MCP server using streamable HTTP
    asyncio.run(mcp.run_streamable_http_async(host="127.0.0.1", port=8001))