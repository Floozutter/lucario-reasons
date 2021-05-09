from requests_html import HTMLSession

def get_poketags() -> tuple[str, ...]:
    session = HTMLSession()
    response = session.get("https://e621.net/wiki_pages/17949")
    all_lists = response.html.find(".expandable", containing = "Generation")
    gen_lists = reversed(all_lists[-8:])
    return tuple(e.text for l in gen_lists for e in l.find("a"))

if __name__ == "__main__":
    with open("poketags.txt", "w", encoding = "utf-8") as ofile:
        for tag in get_poketags():
            ofile.write(tag + "\n")
