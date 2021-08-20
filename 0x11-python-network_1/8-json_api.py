#!/usr/bin/python3
""" task 7 module """

import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    try:
        user = {'q': sys.argv[1]}
    except IndexError:
        user = {'q': ""}
    r = requests.post(url, user)

    if len(r.json()) == 0:
        print("No result")
    else:
        print("[{}] {}".format(r.json().get('id'), r.json().get('name')))
