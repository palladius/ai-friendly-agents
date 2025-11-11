#!/bin/bash

mkdir -p rag/ &&
    git clone https://github.com/google/adk-python rag/adk-python/ || echo already cloned probably..


# Clean: rm -rf rag/adk-python/
