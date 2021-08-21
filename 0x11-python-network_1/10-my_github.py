#!/usr/bin/python3
""" task 7 module """

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == '__main__':
    url = "https://api.github.com/user"
    user = sys.argv[1]
    pwd = sys.argv[2]
    r = requests.get(url, auth=HTTPBasicAuth(user, pwd))
    if len(r.json()) == 0:
        print(None)
    else:
        print("{}".format(r.json().get('id')))
