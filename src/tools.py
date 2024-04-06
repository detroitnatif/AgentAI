import os
from exa_py import Exa
from langchain.agents import tool

class ExaSearchToolset():
    @tool
    def search(query: str):
        """Search for a webpage based on query"""
        return ExaSearchToolset._exa.search(f'{query}', use_autoprompt=True, num_results=3)
    
    @tool
    def find_similar(url: str):
        """Search for a webpage similar to given URL"""
        return ExaSearchToolset._exa.find_similar(url, use_autoprompt=True, num_results=3)
    
    @tool
    def get_contents(ids: str):
        """Get the contents of a webpage"""

        print('ids from params', ids)
        ids = eval(ids)
        contents = str(ExaSearchToolset._exa().get_contents(ids))
        print(contents)
        contents = contents.split('URL:')
        contents = [content[:1000] for content in contents]
        return '\n\n'.join(contents)
    
    def tools():
        ExaSearchToolset.search,
        ExaSearchToolset.find_similar,
        ExaSearchToolset.get_contents
    def _exa():
        return Exa(api_key=os.environ.get('EXA_API_KEY'))