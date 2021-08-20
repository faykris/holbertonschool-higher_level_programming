#!/usr/bin/python3
""" task 0 module """

import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status')
    content = r.content.decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(content)))
    print("\t- content: {}".format(content))
