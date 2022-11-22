#!/usr/bin/python3

import requests

ISS_TRACKER = 'http://api.open-notify.org/iss-now.json'

def main():
    """runtime code"""

    response = requests.get(ISS_TRACKER)

    tracker = response.json()

    lon = tracker["iss_position"]["longitude"]
    lat = tracker["iss_position"]["latitude"]

    print(f"""
    CURRENT LOCATION OF THE ISS:
    Lon: {lon}
    Lat: {lat}
    """)


if __name__ == "__main__":
    main()
