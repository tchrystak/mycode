#!/usr/bin/python3

import requests

                 # oops! wrong URL!! change the address and this will work
library = "https://anapioficeandfire.com/api"

def main():
    response = requests.get(library)

    decodedjson = response.json()

    print(decodedjson)

if __name__ == "__main__":
    main()
