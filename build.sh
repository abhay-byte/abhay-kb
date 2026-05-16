#!/bin/bash
set -e

cd "$(dirname "$0")"

# Build MCP page (combined: overview + server guides)
echo "Building MCP page..."
python3 md_to_html.py AI-Tools/mcp.md /tmp/mcp_content.html
./wrap_html.sh /tmp/mcp_content.html AI-Tools/mcp.html "MCP — Model Context Protocol" "MCP"
echo "✓ Built AI-Tools/mcp.html"

# Rebuild tools page
echo "Rebuilding tools page..."
git show 7f8bc37^:AI-Tools/tools.html | awk 'BEGIN{skip=0} /^---$/{skip++;next} skip>=2{print}' > /tmp/tools_clean.html
./wrap_html.sh /tmp/tools_clean.html AI-Tools/tools.html "AI Coding Tools" "AI Coding Tools"
echo "✓ Built AI-Tools/tools.html"

# Rebuild overview page
echo "Rebuilding overview page..."
git show HEAD:AI-Tools/index.html | awk '/<main class="main-content">/{found=1; next} /<\/main>/{if(found) exit} found{print}' | sed 's/^      //' > /tmp/overview_clean.html
./wrap_html.sh /tmp/overview_clean.html AI-Tools/index.html "AI Tools" "AI Tools"
echo "✓ Built AI-Tools/index.html"

echo "Done! All HTML files created."
