#!/bin/bash

mkdir -p rag/ &&
    git clone https://github.com/google/adk-python rag/adk-python/ || echo already cloned probably..


echo 'ADK python downloaded under rag/adk-python/. To enable Gemini CLI, ensure to setup the respectGitIgnore correctly (see WORKSHOP.md for more)'

# Clean: rm -rf rag/adk-python/
