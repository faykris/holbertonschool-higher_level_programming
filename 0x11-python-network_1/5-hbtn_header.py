#!/usr/bin/python3
""" task 0 module """

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
