#!/usr/bin/python3

import requests

library_books = "https://www.anapioficeandfire.com/api/books"

def main():
    response = requests.get(library_books)

    decodedjson = response.json()

    for book in decodedjson:
        print(f"{book['name']}, pages - {book['numberOfPages']}")
        print(f"\tAPI URL -> {book['url']}\n")
        # print ISBN
        print(f"\tISBN -> {book['isbn']}\n")
        print(f"\tPUBLISHER -> {book['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(book['characters'])}\n")

if __name__ == "__main__":
    main()
