from requests_html import HTMLSession
from time import sleep
from urllib.parse import urlencode
from json import loads
from typing import Iterator, Any

API_POSTS = "https://e621.net/posts.json"

def all_posts(params: dict[str, str], delay: int = 1) -> Iterator[dict[str, Any]]:
    session = HTMLSession()
    page_params = {"limit": "1"}
    while True:
        # get page of posts
        query = urlencode(params | page_params, safe = "+")
        response = session.get(API_POSTS, params = query)
        posts = loads(response.text)["posts"]
        if not posts:
            return
        # yield posts in page
        for post in posts:
            yield post
        # update page
        page_params |= {"limit": "320", "page": f"b{post['id']}"}
        sleep(delay)
