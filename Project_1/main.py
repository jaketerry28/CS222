from wiki import Search, Revisions

def main():
    query = input("Search for Article: ")
    search = Search()
    search.searchWiki(query)

main()