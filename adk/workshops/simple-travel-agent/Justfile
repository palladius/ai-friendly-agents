set shell := ["bash", "-c"]

default: list

# List available commands
list:
    @just --list

# Install dependencies
install:
    uv sync

# Test that all workshop steps can at least be imported (catches syntax/import errors)
test-whole-workshop:
    uv run python test_workshop.py

# Manually test Step 3b with both custom tool + GoogleSearch. Note that `exit 0` cant be trusted we need someone to look at the output. But at least Giancarlo can read stdio.
test-03b-manhouse:
    # 1. Lets check what time is it - current model should use get_now tool
    echo "What time is it?" | uv run adk run steps/step03b_search_and_tool || true
    # 2. Now lets ask for weather in Zurich today
    echo "What is the weather in Zurich today?" | uv run adk run steps/step03b_search_and_tool || true
# --- CLI RUN COMMANDS ---

# Run Step 1: Basic Agent (CLI)
run-step1:
    uv run adk run steps/step01_basic

# Run Step 2: Agent with a custom tool (CLI)
run-step2:
    uv run adk run steps/step02_tool

# Run Step 3: Agent with Google Search (CLI)
run-step3:
    uv run adk run steps/step03_search

# Run Step 3b: Agent with Search and Tool (CLI, different model)
run-step3b:
    uv run adk run steps/step03b_search_and_tool

# Run Step 4: Agent with Airbnb MCP (CLI)
run-step4:
    uv run adk run steps/step04_mcp

# --- USER SOLUTION COMMANDS ---

# Run your solution (CLI)
run-mysolution:
    uv run adk run mysolution/

# Run your solution (Web UI) - Select 'mysolution' in the UI
web-mysolution:
    @echo "REMEMBER to select 'mysolution/' in the UI after it starts"
    uv run adk web .

# --- WEB UI COMMANDS ---

# Run Step 1/2/3/4 in Web UI and logs under log/ ..
web-4steps:
    #uv run adk web steps/
    mkdir -p log && uv run adk web steps/ > log/web.log 2>&1

clean:
    rm -rf .venv/

# Downloads ADK python under rag/
rag:
    ./download-adk.sh

# Testing Gemini CLI 
nanobanana-gen-favicon:
    #!/bin/bash
    export NANOBANANA_MODEL="gemini-3-pro-image-preview"
    echo "Check docs in here: https://github.com/gemini-cli-extensions/nanobanana"
    
    #gemini --yolo -p "/icon 'a funny icon for this workshop' and create a SMALL favicon.ico and a BIGGER workshop.png"
    gemini --yolo -p "/diagram 'Coding steps (read the WORKSHOP.md first)' --type=flowchart --style=professional --preview"