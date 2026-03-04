import importlib
import sys
import os

# Add the current directory to sys.path to make 'steps' importable
sys.path.append(os.getcwd())

steps = [
    "steps.step01_basic.agent",
    "steps.step02_tool.agent",
    "steps.step03_search.agent",
    "steps.step03b_search_and_tool.agent",
    "steps.step04_mcp.agent",
]

failed = False
for step in steps:
    try:
        print(f"Testing import of {step}...")
        importlib.import_module(step)
        print(f"Successfully imported {step}")
    except Exception as e:
        print(f"Failed to import {step}: {e}")
        failed = True

if failed:
    sys.exit(1)
else:
    print("All steps imported successfully!")
    sys.exit(0)
