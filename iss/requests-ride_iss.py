#!/usr/bin/python3
"""Alta3 Research - tracking ISS updated output"""

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    """reading json from api"""
    # call the api
    groundctrl = urllib.request.urlopen(MAJORTOM)

    # strip off the attachment (JSON) and read it
    # the problem here, is that it will read out as a string
    helmet = groundctrl.read()

    helmetson = json.loads(helmet.decode("utf-8"))

    # display people in space
    print("People in space: " + str(helmetson["number"]))

    # display every item in a list
    for astro in helmetson["people"]:
        # display ONLY the name value associated with astro
        print(f'{astro["name"]} on the {astro["craft"]}')
        # check out line 23; the variable we used is "astro" not "person
        # so either change line 26 or line 23 and it will work :)

if __name__ == "__main__":
    main()

