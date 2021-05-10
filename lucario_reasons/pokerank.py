if __name__ == "__main__":
    with open("poketags.txt", "r", encoding = "utf-8") as ifile:
        poketags = tuple(ifile.read().strip().split())
