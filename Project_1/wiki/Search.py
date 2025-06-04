from .ConnectToAPI import ConnectToAPI
from .Revisions import Revisions
# parameters for searching wiki


class Search(ConnectToAPI):
    
    def __init__(self):
        super().__init__("Search")
        self.params = {
          "action": "query",
          "list": "search",
          "srsearch": "",
          "format": "json"
        }
    
    def searchWiki(self, search_page):
        self.params["srsearch"] = search_page
        DATA = super().connect(self.params, self.name)

        # check if search results exists
        if DATA['query']['searchinfo']["totalhits"] == 0:
            print("No search found")
        # if search equals first item in search
        elif DATA['query']['search'][0]['title'].lower() == search_page.lower():
            revisions = Revisions()
            revisions.getRevisions(DATA['query']['search'][0]['title'])
        # redirection
        else:
            newSearch = DATA['query']['search'][0]['title']
            print(f"\nYou were redirected from {search_page} to {newSearch}")
            revisions = Revisions()
            revisions.getRevisions(newSearch)
