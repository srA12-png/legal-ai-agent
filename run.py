#!/usr/bin/env python3
"""
Root entry point for Legal AI Agent (LexBot)
Allows running either the Streamlit Web UI or the Terminal CLI directly from root.

Usage:
    python run.py             # Launches Streamlit Web UI
    python run.py --ui        # Launches Streamlit Web UI
    python run.py --cli       # Runs interactive Terminal CLI
    python run.py --build     # Builds / rebuilds the FAISS vector index
"""

import sys
import os
import subprocess

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
LEGAL_AGENT_DIR = os.path.join(PROJECT_ROOT, "legal-agent")

def main():
    args = sys.argv[1:]
    
    if "--build" in args:
        print("[*] Launching vector index builder...")
        main_py = os.path.join(LEGAL_AGENT_DIR, "main.py")
        sys.exit(subprocess.call([sys.executable, main_py, "--build"]))

    elif "--cli" in args:
        print("[*] Launching Terminal CLI...")
        main_py = os.path.join(LEGAL_AGENT_DIR, "main.py")
        sys.exit(subprocess.call([sys.executable, main_py]))

    else:
        print("[*] Launching LexBot Streamlit Web Interface...")
        app_py = os.path.join(LEGAL_AGENT_DIR, "ui", "app.py")
        cmd = [sys.executable, "-m", "streamlit", "run", app_py]
        try:
            sys.exit(subprocess.call(cmd))
        except KeyboardInterrupt:
            print("\n[*] Exiting LexBot.")

if __name__ == "__main__":
    main()
