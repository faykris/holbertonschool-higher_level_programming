#!/usr/bin/python3
""" task 0 module """
import urllib.request

with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
    html = response.read()
    info_dict = response.info().__dict__
    for h_list in info_dict.values():
        if type(h_list) is list and len(h_list) != 0:
            for h_tu in h_list:
                if h_tu[0] == 'X-Request-Id':
                    print(h_tu[1])
