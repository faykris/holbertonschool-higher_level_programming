#!/usr/bin/python3
""" task 0 module """
import urllib.request
import sys

with urllib.request.urlopen(sys.argv[1]) as response:
    info_dict = response.info().__dict__
    for h_list in info_dict.values():
        if type(h_list) is list and len(h_list) != 0:
            for h_tu in h_list:
                if h_tu[0] == 'X-Request-Id':
                    print(h_tu[1])
