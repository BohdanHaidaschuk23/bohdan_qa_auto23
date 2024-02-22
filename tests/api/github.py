import requests



class Github:

    def get_some_user(self, username):
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()
        return body

    def search_repo(self, name):
        r = requests.get("https://api.github.com/search/repositories?q=Q", params={"q": name})
        body = r.json()
        return body