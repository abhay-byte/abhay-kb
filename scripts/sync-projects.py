#!/usr/bin/env python3
"""
sync-projects.py — Generate PROJECTS.md with featured showcase + full repo stats.

Fetches all public repos for abhay-byte from GitHub API.
Generates PROJECTS.md with:
  - Featured projects showcase (with gifs + screenshots)
  - Stats overview
  - Top 10 by stars
  - Full repository table
  - Language breakdown

Usage: python3 scripts/sync-projects.py
"""

import json
import subprocess
import sys
import os
from datetime import datetime, timezone

# ── Configuration ──────────────────────────────────────────────────────────
REPO_OWNER = "abhay-byte"

# Each featured project: (repo_name, label, logo_url, description, gif_url, screenshot_url, badges_list)
FEATURED = [
    ("fluxlinux", "FluxLinux",
     "https://raw.githubusercontent.com/abhay-byte/fluxlinux/main/assets/logo/logo.webp",
     "Run full Linux desktop environments on Android with GPU acceleration and dev stacks.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/fluxlinux.gif", None,
     ["[![Play Store](https://img.shields.io/badge/Play_Store-01875F?style=flat-square&logo=googleplay&logoColor=white)](https://play.google.com/store/apps/details?id=com.zenithblue.fluxlinux)",
      "[![F-Droid](https://img.shields.io/badge/F--Droid-1976D2?style=flat-square&logo=f-droid&logoColor=white)](https://f-droid.org/packages/com.ivarna.fluxlinux)"]),

    ("finalbenchmark-platform", "FinalBenchmark 2",
     "https://raw.githubusercontent.com/abhay-byte/finalbenchmark-platform/main/assets/logo_2.png",
     "Comprehensive CPU benchmarking app with 10+ tests and thermal management.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/FinalBenchmark2.gif", None,
     ["[![F-Droid](https://img.shields.io/badge/F--Droid-1976D2?style=flat-square&logo=f-droid&logoColor=white)](https://f-droid.org/packages/com.ivarna.finalbenchmark2)"]),

    ("mkm", "MKM",
     "https://github.com/abhay-byte/mkm/raw/main/assets/logo.png",
     "Minimal Kernel Manager for persistent swap management with Shizuku support.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/MKM.gif",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/mkm-screenshot.png",
     ["[![Play Store](https://img.shields.io/badge/Play_Store-01875F?style=flat-square&logo=googleplay&logoColor=white)](https://play.google.com/store/apps/details?id=com.ivarna.mkm)",
      "[![F-Droid](https://img.shields.io/badge/F--Droid-1976D2?style=flat-square&logo=f-droid&logoColor=white)](https://f-droid.org/packages/com.ivarna.mkm)"]),

    ("nexus", "Nexus Terminal",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/nexus-logo.png",
     "Multi-agent AI terminal workspace — run Claude Code, Codex CLI, Gemini CLI, Qwen, Aider, and more side-by-side.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/nexus.gif", None, []),

    ("planet-racing", "Fantasy Racing",
     "https://raw.githubusercontent.com/abhay-byte/threejs_portfolio/main/public/images/fantasy-racing-icon.png",
     "High-speed futuristic racing game with diverse planets, strategic challenges, and immersive gameplay.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/fantasy-racing.gif", None,
     ["[![Unity](https://img.shields.io/badge/Unity-100000?style=flat-square&logo=unity&logoColor=white)](https://unity.com)"]),

    ("Saiko-no-senshi-0.1v", "Story of Xirsia",
     "https://raw.githubusercontent.com/abhay-byte/threejs_portfolio/main/public/images/xirsia-icon.png",
     "2D Role Playing Game set in Medieval age with a massive 25km² open world of Xirsia Isle to explore.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/xirsia.gif", None,
     ["[![Play Game](https://img.shields.io/badge/Play_Game-FF6B6B?style=flat-square&logo=unity&logoColor=white)](https://hind-dev.web.app/#/)"]),

    ("phone_finder_hub", "Phone Finder Hub",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/phonefinder-logo.png",
     "Data-driven smartphone comparison platform built with Laravel. Identify best value-for-money devices via objective performance benchmarks vs current market prices.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/phonefinder-demo.gif", None,
     ["[![Website](https://img.shields.io/badge/Website-FF2D20?style=flat-square&logo=laravel&logoColor=white)](https://phone-finder-shjs.onrender.com/)"]),

    ("Adirstat", "Adirstat",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/adirstat-icon.png",
     "Android Disk Space Analyzer (WizTree/WinDirStat equivalent).",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/adirstat.gif",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/adirstat-feature.png",
     ["[![Play Store](https://img.shields.io/badge/Play_Store-01875F?style=flat-square&logo=googleplay&logoColor=white)](https://play.google.com/store/apps/details?id=com.ivarna.adirstat)"]),

    ("DeviceInsight", "DeviceInsight",
     "https://github.com/abhay-byte/DeviceInsight/raw/master/assets/logo.webp",
     "Premium system monitoring with glassmorphism UI and real-time analytics for CPU, RAM, Storage, Network, and Battery.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/DeviceInsight.gif",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/deviceinsight-screenshot.png", []),

    ("valentines-day-unity", "Whispers in the Mist",
     None,
     "Horror game set in St. Xavier's Boarding School in Ooty during Valentine's Day with mysterious occurrences.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/whispers.gif", None, []),

    ("minor-project-gtbit", "Clinico",
     "https://github.com/abhay-byte/minor-project-gtbit/raw/main/assets/logo/Clinico%20Logo.png",
     "AI-powered healthcare platform with 24/7 AI companion, telehealth, and hyperlocal clinic discovery.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/clinico.gif",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/clinico-app-screenshot.png",
     ["[![Website](https://img.shields.io/badge/Website-00C7B7?style=flat-square&logo=react&logoColor=white)](https://clinicofrontend.onrender.com/)",
      "[![Backend](https://img.shields.io/badge/Backend-68A063?style=flat-square&logo=node.js&logoColor=white)](https://minor-project-gtbit.onrender.com/)",
      "[![AI](https://img.shields.io/badge/AI-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)](https://clinico-ai-service.onrender.com/)",
      "[![Figma](https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=figma&logoColor=white)](https://www.figma.com/design/dFDrEe30gtdNb1QFVKWNv2/Clinico---UI-UX)"]),

    ("warden-protocol", "Warden Protocol",
     "https://raw.githubusercontent.com/abhay-byte/warden-protocol/refs/heads/master/assets/icon.png",
     "Single-player Android strategy game where you act as bunker intelligence for survivors.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/warden-protocol.gif", None,
     ["[![Play Store](https://img.shields.io/badge/Play_Store-01875F?style=flat-square&logo=googleplay&logoColor=white)](https://play.google.com/store/apps/details?id=com.ivarna.wardenprotocol)"]),

    ("nativecode", "NativeCode",
     "https://raw.githubusercontent.com/abhay-byte/nativecode/master/assets/logo/logo.webp",
     "Local AI development environment on Android — run LLMs, code editors, and dev tools on-device.",
     None,
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/NativeCode.png", []),

    ("TaskStack", "TaskStack",
     "https://raw.githubusercontent.com/abhay-byte/TaskStack/main/assets/images/app_icon.png",
     "Next-generation daily task management app with a 24-hour visual timeline and life analytics.",
     None, None, []),

    ("AllWidgets", "AllWidgets",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/allwidgets-icon.png",
     "Widget suite with polished home-screen experiences for multiple device skins.",
     None,
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/allwidgets-feature.png", []),

    ("truvalt", "Truvalt",
     "https://raw.githubusercontent.com/abhay-byte/truvalt/main/assets/truvalt_icon.png",
     "Secure, self-hostable, zero-knowledge password manager for Android and web.",
     None, None, []),

    ("apm", "APM",
     None,
     "Android package manager — install, batch-install, and manage APKs on Android devices via ADB.",
     None,
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/apm.jpg", []),

    ("threejs_portfolio", "ThreeJS Portfolio",
     "https://raw.githubusercontent.com/abhay-byte/my-portfolio/main/public/favicon.ico",
     "Interactive 3D portfolio website built with Three.js (React Three Fiber).",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/threejs-portfolio.gif",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/webgl-screenshot.png",
     ["[![Website](https://img.shields.io/badge/Website-fabd2f?style=flat-square&logo=three.js&logoColor=282828)](https://abhay-byte.web.app/)"]),

    ("my-portfolio", "My Portfolio",
     None,
     "Personal portfolio website showcasing projects, skills, and experience with responsive design.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/my-portfolio.gif", None,
     ["[![Website](https://img.shields.io/badge/Website-fabd2f?style=flat-square&logo=react&logoColor=282828)](https://abhayraj-porfolio.web.app/)"]),

    ("webgl-website", "WebGL Website",
     None,
     "Interactive website built with WebGL for stunning 3D graphics and animations.",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/webgl.gif",
     "https://raw.githubusercontent.com/abhay-byte/abhay-byte/main/assets/webgl-screenshot.png",
     ["[![Website](https://img.shields.io/badge/Website-fabd2f?style=flat-square&logo=webgl&logoColor=282828)](https://abhay-raj.web.app/)"]),
]

KB_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_FILE = os.path.join(KB_DIR, "PROJECTS.md")
BUILD_SCRIPT = os.path.join(KB_DIR, "build.sh")


def run_gh_api(endpoint):
    """Run gh api and return parsed JSON."""
    result = subprocess.run(
        ["gh", "api", endpoint, "--paginate"],
        capture_output=True, text=True, check=True
    )
    lines = result.stdout.strip().splitlines()
    repos = []
    for line in lines:
        try:
            data = json.loads(line)
            if isinstance(data, list):
                repos.extend(data)
            else:
                repos.append(data)
        except json.JSONDecodeError:
            pass
    return repos


def fetch_repos():
    """Fetch all repos for the owner using gh api."""
    repos = run_gh_api(f"users/{REPO_OWNER}/repos?per_page=100&type=all&sort=pushed")
    if not repos:
        print("[ERROR] No repos found. Check auth and owner name.", file=sys.stderr)
        sys.exit(1)
    return repos


def compute_stats(repos):
    """Compute aggregate stats from repo list."""
    total = len(repos)
    total_stars = sum(r.get("stargazers_count", 0) for r in repos)
    total_forks = sum(r.get("forks_count", 0) for r in repos)

    lang_repo_count = {}
    lang_star_count = {}
    for r in repos:
        lang = r.get("language") or "—"
        stars = r.get("stargazers_count", 0)
        lang_repo_count[lang] = lang_repo_count.get(lang, 0) + 1
        lang_star_count[lang] = lang_star_count.get(lang, 0) + stars

    languages_used = len([l for l in lang_repo_count if l != "—"])

    sorted_langs = sorted(lang_star_count.items(), key=lambda x: -x[1])
    top_lang = sorted_langs[0][0] if sorted_langs else "—"
    top_lang_stars = sorted_langs[0][1] if sorted_langs else 0
    top_lang_repos = lang_repo_count.get(top_lang, 0)

    return {
        "total": total,
        "total_stars": total_stars,
        "total_forks": total_forks,
        "languages_used": languages_used,
        "top_lang": top_lang,
        "top_lang_stars": top_lang_stars,
        "top_lang_repos": top_lang_repos,
        "lang_repo_count": lang_repo_count,
        "lang_star_count": lang_star_count,
    }


import re as _re

EMOJI_PATTERN = _re.compile(
    '[\U0001F600-\U0001F64F'  # emoticons
    '\U0001F300-\U0001F5FF'  # symbols & pictographs
    '\U0001F680-\U0001F6FF'  # transport & map symbols
    '\U0001F1E0-\U0001F1FF'  # flags
    '\U00002702-\U000027B0'  # dingbats
    '\U000024C2-\U0001F251'
    ']+'
)

def clean_str(val):
    """Return string with emojis stripped."""
    if not val:
        return ""
    return EMOJI_PATTERN.sub('', str(val)).strip()


def safe_str(val):
    return clean_str(val) if val else ""





def build_featured_section(repos_by_name):
    """Build the featured projects showcase as pure markdown tables."""
    lines = []
    lines.append("## Featured Projects\n")

    for key, label, logo, desc, gif_url, screenshot_url, badges in FEATURED:
        repo = repos_by_name.get(key)
        gh_url = f"https://github.com/{REPO_OWNER}/{key}"

        # Skip if repo doesn't exist
        exists = repo is not None
        stars = repo.get("stargazers_count", 0) if exists else 0
        forks = repo.get("forks_count", 0) if exists else 0
        lang = repo.get("language", "—") if exists else "—"

        # Header with logo
        if logo:
            lines.append(f'<img src="{logo}" width="28" align="absmiddle" alt="{label}"/>')
        lines.append(f"### [{label}]({gh_url})")
        lines.append("")

        # Description
        lines.append(f"{desc}")
        lines.append("")

        # Stats inline
        stat_parts = []
        if stars > 0:
            stat_parts.append(f"**{stars}** stars")
        if forks > 0:
            stat_parts.append(f"**{forks}** forks")
        if lang and lang != "—":
            stat_parts.append(f"{lang}")
        if stat_parts:
            lines.append(" ".join(stat_parts))
            lines.append("")

        # Badges
        badge_parts = [f"[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github)]({gh_url})"]
        badge_parts.extend(badges)
        if stars > 0:
            badge_parts.append(f"[![Stars](https://img.shields.io/github/stars/{REPO_OWNER}/{key}?style=flat-square&labelColor=282828&color=fabd2f&logo=github&logoColor=white)]({gh_url}/stargazers)")
        lines.append(" ".join(badge_parts))
        lines.append("")

        # Screenshot (if available)
        if screenshot_url:
            lines.append(f"![Screenshot - {label}]({screenshot_url})")
            lines.append("")

        # GIF (if available)
        if gif_url:
            lines.append(f"![Demo - {label}]({gif_url})")
            lines.append("")

        lines.append("---\n")

    return "\n".join(lines)


def build_stats_table(stats):
    """Build the stats overview table."""
    lines = []
    lines.append("## Stats Overview\n")
    lines.append("| Metric | Value |")
    lines.append("|---|---|")
    lines.append(f"| **Total Repositories** | {stats['total']} |")
    lines.append(f"| **Total Stars** | {stats['total_stars']} |")
    lines.append(f"| **Total Forks** | {stats['total_forks']} |")
    lines.append(f"| **Languages Used** | {stats['languages_used']} |")
    lines.append(f"| **Top Language** | {stats['top_lang']} ({stats['top_lang_stars']} stars, {stats['top_lang_repos']} repos) |")
    lines.append("")
    return "\n".join(lines)


def build_top10(repos_sorted):
    """Build the top 10 by stars table."""
    lines = []
    lines.append("## Top Projects by Stars\n")
    lines.append("| # | Project | Stars | Forks | Language | Description |")
    lines.append("|---|---|---|---|---|---|")
    for i, r in enumerate(repos_sorted[:10], 1):
        name = r["name"]
        desc = safe_str(r.get("description", ""))
        lang = r.get("language") or "—"
        stars = r["stargazers_count"]
        forks = r["forks_count"]
        url = f"https://github.com/{REPO_OWNER}/{name}"
        lines.append(f"| {i} | [{name}]({url}) | {stars} | {forks} | {lang} | {desc} |")
    lines.append("")
    return "\n".join(lines)


def build_full_table(repos_sorted):
    """Build full repository listing."""
    lines = []
    lines.append("## All Repositories\n")
    lines.append("| Project | Stars | Forks | Language | Description |")
    lines.append("|---|---|---|---|---|")

    for r in repos_sorted:
        name = r["name"]
        desc = safe_str(r.get("description", ""))
        lang = r.get("language") or "—"
        stars = r["stargazers_count"]
        forks = r["forks_count"]
        url = f"https://github.com/{REPO_OWNER}/{name}"
        lines.append(f"| [{name}]({url}) | {stars} | {forks} | {lang} | {desc} |")

    lines.append("")
    return "\n".join(lines)


def build_language_breakdown(stats):
    """Build language breakdown table."""
    lines = []
    lines.append("## Language Breakdown\n")
    lines.append("| Language | Repos | Stars |")
    lines.append("|---|---|---|")

    sorted_langs = sorted(stats["lang_star_count"].items(), key=lambda x: -x[1])
    for lang, star_count in sorted_langs:
        repo_count = stats["lang_repo_count"].get(lang, 0)
        star_str = str(star_count) if star_count > 0 else "0"
        lines.append(f"| {lang} | {repo_count} | {star_str} |")

    lines.append("")
    return "\n".join(lines)


def main():
    print("Fetching repos from GitHub API...")
    repos = fetch_repos()
    print(f"   [OK] Found {len(repos)} repos")

    repos_sorted = sorted(repos, key=lambda r: -r.get("stargazers_count", 0))
    repos_by_name = {r["name"]: r for r in repos}

    stats = compute_stats(repos)
    print(f"   [OK] Stats computed: {stats['total_stars']} total stars, {stats['languages_used']} languages")

    # Build content
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    content_parts = []

    # Frontmatter
    content_parts.append("---")
    content_parts.append("layout: standalone")
    content_parts.append('title: "Projects Dashboard"')
    content_parts.append("---")
    content_parts.append("")
    content_parts.append(f"# Projects Dashboard\n")
    content_parts.append(f"> **Last synced:** {now_utc} — **{stats['total']} repos** — **{stats['total_stars']} total stars**\n")

    # Featured showcase
    content_parts.append(build_featured_section(repos_by_name))

    # Stats
    content_parts.append(build_stats_table(stats))

    # Top 10
    content_parts.append(build_top10(repos_sorted))

    # Full table
    content_parts.append(build_full_table(repos_sorted))

    # Language breakdown
    content_parts.append(build_language_breakdown(stats))

    # Footer
    content_parts.append("---")
    content_parts.append(f"Auto-generated by Reva on {now_utc}")
    content_parts.append("")

    final_content = "\n".join(content_parts)

    with open(OUTPUT_FILE, "w") as f:
        f.write(final_content)
    print(f"   [OK] Written to {OUTPUT_FILE}")

    # Run build
    print("\nRunning build.sh...")
    try:
        subprocess.run(["bash", BUILD_SCRIPT], cwd=KB_DIR, check=True, capture_output=True, text=True)
        print("   [OK] Build complete")
    except subprocess.CalledProcessError as e:
        print(f"   [WARN] Build failed: {e.stderr.strip() or e.stdout.strip()}")

    print("\n[DONE] PROJECTS.md generated successfully.")


if __name__ == "__main__":
    main()
