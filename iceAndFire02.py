#!/usr/bin/python3

import pprint
import requests

library_books = "https://www.anapioficeandfire.com/api/books"

def main():
    response = requests.get(library_books)
    
    decodedjson = response.json()

    pprint.pprint(decodedjson)

if __name__ == "__main__":
    main()
