#!/usr/bin/python3
""" task 0 module """

import requests
import sys

url = sys.argv[1]
if __name__ == '__main__':
    r = requests.get(url)
    print(r.headers['X-Request-Id'])
