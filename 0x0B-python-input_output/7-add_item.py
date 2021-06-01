#!/usr/bin/python3
"""----- 7. Load, add, save -----
    Write a script that adds all arguments to a Python list,
    and then save them to a file.
"""
import sys
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
filename = "add_item.json"
i = 0

try:
    with open(filename, 'r') as file:
        file.close()
except FileNotFoundError:
    with open(filename, 'w') as file:
        file.write("[]")
        file.close()

py_file = load_from_json_file(filename)
for arg in sys.argv:
    if i != 0:
        py_file.append(sys.argv[i])
    i += 1
save_to_json_file(py_file, filename)
