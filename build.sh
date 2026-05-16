#!/bin/bash

set -e

cd "$(dirname "$0")"

# Build MCP page
echo "Building MCP page..."
python3 md_to_html.py AI-Tools/mcp.md /tmp/mcp_content.html

cat > AI-Tools/mcp.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MCP | Abhay's Knowledge Base</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #0d0d0d;
      color: #e0e0e0;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      line-height: 1.6;
    }
    a { color: #fabd2f; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .page-wrapper { display: flex; max-width: 1200px; margin: 0 auto; padding: 40px 24px; gap: 40px; min-height: 100vh; }
    .topbar {
      display: none;
      position: fixed; top: 0; left: 0; right: 0;
      height: 52px;
      background: #0d0d0d;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      align-items: center;
      padding: 0 16px;
      z-index: 100;
    }
    .hamburger {
      background: none; border: none; color: #fff; font-size: 24px;
      cursor: pointer; padding: 4px 8px; margin-right: 12px;
    }
    .topbar-title { font-size: 16px; font-weight: 600; color: #fff; }
    .sidebar-overlay {
      display: none;
      position: fixed; inset: 0;
      background: rgba(0,0,0,0.6);
      z-index: 150;
    }
    .sidebar-overlay.active { display: block; }
    .sidebar {
      width: 260px; flex-shrink: 0; display: flex; flex-direction: column;
      position: sticky; top: 40px; align-self: flex-start; min-height: calc(100vh - 80px);
    }
    .sidebar h1 {
      font-size: 22px; font-weight: 700; color: #fff;
      margin-bottom: 4px;
    }
    .sidebar .tagline { font-size: 14px; color: #888; margin-bottom: 24px; }
    .sidebar nav { display: flex; flex-direction: column; gap: 2px; flex: 1; }
    .sidebar nav a {
      display: block; padding: 8px 12px; border-radius: 6px;
      color: #ccc; font-size: 15px;
      transition: background 0.15s;
    }
    .sidebar nav a:hover { background: rgba(255,255,255,0.06); color: #fff; text-decoration: none; }
    .nav-section-label {
      font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px;
      color: #666; padding: 12px 12px 4px; margin-top: 4px;
    }
    .nav-indent { padding-left: 28px !important; font-size: 14px !important; }
    .main-content { flex: 1; min-width: 0; }
    .main-content h1 { font-size: 32px; font-weight: 700; color: #fff; margin-bottom: 16px; }
    .main-content h2 { font-size: 22px; font-weight: 600; color: #fff; margin: 32px 0 16px; }
    .main-content h3 { font-size: 18px; font-weight: 600; color: #fff; margin: 24px 0 12px; }
    .main-content p { margin-bottom: 16px; font-size: 16px; color: #ccc; }
    .main-content ul, .main-content ol { margin: 0 0 16px 20px; }
    .main-content li { margin-bottom: 6px; color: #ccc; }
    .main-content table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px; }
    .main-content th, .main-content td { text-align: left; padding: 8px 12px; border-bottom: 1px solid rgba(255,255,255,0.08); }
    .main-content th { color: #fff; font-weight: 600; background: rgba(255,255,255,0.04); }
    .main-content td { color: #ccc; }
    .main-content tr:hover td { background: rgba(255,255,255,0.02); }
    .main-content code { background: rgba(255,255,255,0.06); padding: 2px 6px; border-radius: 4px; font-size: 13px; color: #fabd2f; }
    .main-content pre { background: rgba(0,0,0,0.3); padding: 16px; border-radius: 6px; overflow-x: auto; margin: 16px 0; }
    .main-content pre code { background: none; padding: 0; color: #fabd2f; }
    .main-content em { color: #999; }
    .main-content strong { color: #fff; }
    hr { border: none; border-top: 2px solid rgba(255,255,255,0.12); margin: 32px 0; }

    @media (max-width: 800px) {
      .page-wrapper { padding: 72px 16px 40px; flex-direction: column; }
      .sidebar { display: none; position: fixed; left: 0; top: 0; bottom: 0; width: 280px; background: #0d0d0d; z-index: 200; padding: 20px; }
      .sidebar.open { display: flex; }
      .topbar { display: flex; }
    }
  </style>
</head>
<body>
  <div class="topbar">
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="topbar-title">MCP</div>
  </div>

  <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>

  <div class="page-wrapper">
    <aside class="sidebar" id="sidebar">
      <h1>Abhay's KB</h1>
      <div class="tagline">My personal projects and notes</div>
      <nav>
        <a href="/abhay-kb/">Home</a>

        <div class="nav-section-label">🤖 LLM</div>
        <a href="/abhay-kb/LLM/models" class="nav-indent">Models</a>
        <a href="/abhay-kb/LLM/coding-plans" class="nav-indent">Coding Plans</a>

        <div class="nav-section-label">AI Tools</div>
        <a href="/abhay-kb/AI-Tools/" class="nav-indent">Overview</a>
        <a href="/abhay-kb/AI-Tools/tools.html" class="nav-indent">Tools</a>
        <a href="/abhay-kb/AI-Tools/mcp.html" class="nav-indent">MCP</a>
        <a href="/abhay-kb/AI-Tools/mcp-servers.html" class="nav-indent">MCP Servers</a>
        <a href="/abhay-kb/AI-Tools/ai-editors.html" class="nav-indent">AI Editors</a>
        <a href="/abhay-kb/AI-Tools/skills.html" class="nav-indent">Skills</a>

        <div class="nav-section-label">📁 Projects</div>
        <a href="/abhay-kb/PROJECTS.html" class="nav-indent">Projects</a>

        <div class="nav-section-label">👤 About</div>
        <a href="/abhay-kb/about-me" class="nav-indent">About Me</a>
      </nav>
    </aside>

    <main class="main-content">
EOF

cat /tmp/mcp_content.html >> AI-Tools/mcp.html

cat >> AI-Tools/mcp.html << 'EOF'
    </main>
  </div>

  <script>
    function toggleSidebar() {
      document.getElementById('sidebar').classList.toggle('open');
      document.getElementById('sidebarOverlay').classList.toggle('active');
    }
  </script>
</body>
</html>
EOF

echo "✓ Built AI-Tools/mcp.html"

# Build MCP servers page
echo "Building MCP Servers page..."
python3 md_to_html.py AI-Tools/mcp-servers.md /tmp/mcp-servers_content.html

cat > AI-Tools/mcp-servers.html << 'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>MCP Servers | Abhay's Knowledge Base</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      background: #0d0d0d;
      color: #e0e0e0;
      font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
      line-height: 1.6;
    }
    a { color: #fabd2f; text-decoration: none; }
    a:hover { text-decoration: underline; }
    .page-wrapper { display: flex; max-width: 1200px; margin: 0 auto; padding: 40px 24px; gap: 40px; min-height: 100vh; }
    .topbar {
      display: none;
      position: fixed; top: 0; left: 0; right: 0;
      height: 52px;
      background: #0d0d0d;
      border-bottom: 1px solid rgba(255,255,255,0.08);
      align-items: center;
      padding: 0 16px;
      z-index: 100;
    }
    .hamburger {
      background: none; border: none; color: #fff; font-size: 24px;
      cursor: pointer; padding: 4px 8px; margin-right: 12px;
    }
    .topbar-title { font-size: 16px; font-weight: 600; color: #fff; }
    .sidebar-overlay {
      display: none;
      position: fixed; inset: 0;
      background: rgba(0,0,0,0.6);
      z-index: 150;
    }
    .sidebar-overlay.active { display: block; }
    .sidebar {
      width: 260px; flex-shrink: 0; display: flex; flex-direction: column;
      position: sticky; top: 40px; align-self: flex-start; min-height: calc(100vh - 80px);
    }
    .sidebar h1 {
      font-size: 22px; font-weight: 700; color: #fff;
      margin-bottom: 4px;
    }
    .sidebar .tagline { font-size: 14px; color: #888; margin-bottom: 24px; }
    .sidebar nav { display: flex; flex-direction: column; gap: 2px; flex: 1; }
    .sidebar nav a {
      display: block; padding: 8px 12px; border-radius: 6px;
      color: #ccc; font-size: 15px;
      transition: background 0.15s;
    }
    .sidebar nav a:hover { background: rgba(255,255,255,0.06); color: #fff; text-decoration: none; }
    .nav-section-label {
      font-size: 12px; text-transform: uppercase; letter-spacing: 1.5px;
      color: #666; padding: 12px 12px 4px; margin-top: 4px;
    }
    .nav-indent { padding-left: 28px !important; font-size: 14px !important; }
    .main-content { flex: 1; min-width: 0; }
    .main-content h1 { font-size: 32px; font-weight: 700; color: #fff; margin-bottom: 16px; }
    .main-content h2 { font-size: 22px; font-weight: 600; color: #fff; margin: 32px 0 16px; }
    .main-content h3 { font-size: 18px; font-weight: 600; color: #fff; margin: 24px 0 12px; }
    .main-content p { margin-bottom: 16px; font-size: 16px; color: #ccc; }
    .main-content ul, .main-content ol { margin: 0 0 16px 20px; }
    .main-content li { margin-bottom: 6px; color: #ccc; }
    .main-content table { width: 100%; border-collapse: collapse; margin: 16px 0; font-size: 14px; }
    .main-content th, .main-content td { text-align: left; padding: 8px 12px; border-bottom: 1px solid rgba(255,255,255,0.08); }
    .main-content th { color: #fff; font-weight: 600; background: rgba(255,255,255,0.04); }
    .main-content td { color: #ccc; }
    .main-content tr:hover td { background: rgba(255,255,255,0.02); }
    .main-content code { background: rgba(255,255,255,0.06); padding: 2px 6px; border-radius: 4px; font-size: 13px; color: #fabd2f; }
    .main-content pre { background: rgba(0,0,0,0.3); padding: 16px; border-radius: 6px; overflow-x: auto; margin: 16px 0; }
    .main-content pre code { background: none; padding: 0; color: #fabd2f; }
    .main-content em { color: #999; }
    .main-content strong { color: #fff; }
    hr { border: none; border-top: 2px solid rgba(255,255,255,0.12); margin: 32px 0; }

    @media (max-width: 800px) {
      .page-wrapper { padding: 72px 16px 40px; flex-direction: column; }
      .sidebar { display: none; position: fixed; left: 0; top: 0; bottom: 0; width: 280px; background: #0d0d0d; z-index: 200; padding: 20px; }
      .sidebar.open { display: flex; }
      .topbar { display: flex; }
    }
  </style>
</head>
<body>
  <div class="topbar">
    <button class="hamburger" onclick="toggleSidebar()">☰</button>
    <div class="topbar-title">MCP Servers</div>
  </div>

  <div class="sidebar-overlay" id="sidebarOverlay" onclick="toggleSidebar()"></div>

  <div class="page-wrapper">
    <aside class="sidebar" id="sidebar">
      <h1>Abhay's KB</h1>
      <div class="tagline">My personal projects and notes</div>
      <nav>
        <a href="/abhay-kb/">Home</a>

        <div class="nav-section-label">🤖 LLM</div>
        <a href="/abhay-kb/LLM/models" class="nav-indent">Models</a>
        <a href="/abhay-kb/LLM/coding-plans" class="nav-indent">Coding Plans</a>

        <div class="nav-section-label">AI Tools</div>
        <a href="/abhay-kb/AI-Tools/" class="nav-indent">Overview</a>
        <a href="/abhay-kb/AI-Tools/tools.html" class="nav-indent">Tools</a>
        <a href="/abhay-kb/AI-Tools/mcp.html" class="nav-indent">MCP</a>
        <a href="/abhay-kb/AI-Tools/mcp-servers.html" class="nav-indent">MCP Servers</a>
        <a href="/abhay-kb/AI-Tools/ai-editors.html" class="nav-indent">AI Editors</a>
        <a href="/abhay-kb/AI-Tools/skills.html" class="nav-indent">Skills</a>

        <div class="nav-section-label">📁 Projects</div>
        <a href="/abhay-kb/PROJECTS.html" class="nav-indent">Projects</a>

        <div class="nav-section-label">👤 About</div>
        <a href="/abhay-kb/about-me" class="nav-indent">About Me</a>
      </nav>
    </aside>

    <main class="main-content">
EOF

cat /tmp/mcp-servers_content.html >> AI-Tools/mcp-servers.html

cat >> AI-Tools/mcp-servers.html << 'EOF'
    </main>
  </div>

  <script>
    function toggleSidebar() {
      document.getElementById('sidebar').classList.toggle('open');
      document.getElementById('sidebarOverlay').classList.toggle('active');
    }
  </script>
</body>
</html>
EOF

echo "✓ Built AI-Tools/mcp-servers.html"

echo "Done! All HTML files created."
