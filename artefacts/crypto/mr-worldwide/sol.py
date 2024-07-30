#!/usr/bin/env python3

import requests, re

f = open("message.txt")

encoded = f.read()

API_KEY= "894754837956611136633x91773"

def get_letter_from_coordinate(match):
    lat = match.group(1)
    long = match.group(2)
    r = requests.get("https://geocode.xyz/{},{}?json=1&auth={}".format(lat, long, API_KEY))
    j = r.json()
    return j["geocode"][0]

print(re.sub(r'\(([\d\.-]+), ([\d\.-]+)\)', get_letter_from_coordinate, encoded))
