
list:
    just -l


migration-6jun:
    bin/migration-6jun.sh


# Runs the MCP Inspector. Probably slitens on pt 6277 but u care about http://localhost:6274/#resources
mcp-inspector:
    npx @modelcontextprotocol/inspector


download-adk:
    git clone https://github.com/google/adk-python rag/adk-python/ || echo already cloned probably..
    #git clone https://github.com/google/adk-go rag/adk-go/ || echo already cloned probably..
    #git clone https://github.com/google/adk-java rag/adk-java/ || echo already cloned probably..
    cp  rag/adk-python/llms-full.txt rag/adk-python.llms.txt

