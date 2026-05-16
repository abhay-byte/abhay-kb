#!/bin/bash
set -e

cd "$(dirname "$0")"

# Build MCP page
echo "Building MCP page..."
python3 md_to_html.py AI-Tools/mcp.md /tmp/mcp_content.html
./wrap_html.sh /tmp/mcp_content.html AI-Tools/mcp.html "MCP" "MCP"

echo "✓ Built AI-Tools/mcp.html"

# Build MCP servers page
echo "Building MCP Servers page..."
python3 md_to_html.py AI-Tools/mcp-servers.md /tmp/mcp-servers_content.html
./wrap_html.sh /tmp/mcp-servers_content.html AI-Tools/mcp-servers.html "MCP Servers" "MCP Servers"

echo "✓ Built AI-Tools/mcp-servers.html"

# Rebuild tools page from remote (if needed)
echo "Rebuilding tools page..."
curl -s "https://raw.githubusercontent.com/abhay-byte/abhay-kb/main/AI-Tools/tools.html" | \
  awk 'BEGIN{skip=0} /^---$/{skip++;next} skip==1 && /^---$/{skip++;next} skip>=2 && !/^<script>/{print} /^<script>/{exit}' > /tmp/tools_clean.html
./wrap_html.sh /tmp/tools_clean.html AI-Tools/tools.html "AI Coding Tools" "AI Coding Tools"

echo "✓ Built AI-Tools/tools.html"

echo "Done! All HTML files created."
