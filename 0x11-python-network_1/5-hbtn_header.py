#!/usr/bin/python3
""" task 5 module """

import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
