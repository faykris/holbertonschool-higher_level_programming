#!/usr/bin/python3
""" task 7 module """

import requests
import sys

if __name__ == '__main__':
    r = requests.get(sys.argv[1])
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.content.decode('utf-8'))
