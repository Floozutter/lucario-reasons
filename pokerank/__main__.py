from requests_html import HTMLSession
from time import sleep
from urllib.parse import urlencode
from json import loads

API = "https://e621.net/posts.json"
DELAY = 10

def count_search(search: str) -> int:
    count = 0
    session = HTMLSession()
    params_base = {"tags": search, "limit": 320}
    params_page = {}
    while (posts := loads(session.get(API, params = urlencode(
        params_base | params_page, safe = "+"
    )).text)["posts"]):
        count += len(posts)
        last_id = posts[-1]["id"]
        params_page["page"] = f"b{last_id}"
        sleep(DELAY)
    return count

if __name__ == "__main__":
    with open("poketags.txt", "r", encoding = "utf-8") as ifile:
        poketags = tuple(ifile.read().strip().split())
