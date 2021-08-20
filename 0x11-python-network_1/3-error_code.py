#!/usr/bin/python3
""" task 0 module """
import urllib.request
import urllib.parse
import urllib.error
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            the_page = response.read()
            print(the_page.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
