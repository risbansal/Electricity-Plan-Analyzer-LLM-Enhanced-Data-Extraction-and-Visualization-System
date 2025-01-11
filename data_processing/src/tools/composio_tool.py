from composio_crewai import ComposioToolSet, App
# from composio import actions, apps

# composio_tools = ComposioToolSet().get_tools(apps=[App.CODEINTERPRETER])
# composio_tools = ComposioToolSet().get_tools(apps=[App.GITHUB])
composio_tools = ComposioToolSet().get_tools(apps=[App.FILETOOL])

# change App.CODEINTERPRETER to be the app you want to use
# For more info on tool selection, see https://docs.agentstack.sh/tools/tool/composio
# composio_toolset = ComposioToolSet(api_key="gvfxh94bqcvsrrvnn9zeed")

# toolset = ComposioToolSet(entity_id="ytrun", api_key=os.getenv("COMPOSIO_API_KEY"))
# entity