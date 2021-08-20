#!/usr/bin/python3
""" task 0 module """
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.info().get('X-Request-Id'))
