import requests

class ConnectToAPI:

    _URL = "https://en.wikipedia.org/w/api.php"

    @property
    def URL(self):
        return self._URL
    
    def __init__(self, name):
        self.name = name

    def connect(self, params, name):
        try:
            session = requests.Session()
            response = session.get(url=self.URL, params=params)
            data = response.json()

            print(f"\n{name} URL: {response.url}\n")
            return data
        except requests.exceptions.RequestException as e:
            print("Request failed:", e)
