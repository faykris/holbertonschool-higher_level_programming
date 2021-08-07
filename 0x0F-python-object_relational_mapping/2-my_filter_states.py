#!/usr/bin/python3
"""
2. Filter states by user input
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name = '" + str(sys.argv[4]) +\
          "' ORDER BY id ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        print("({}: '{}')".format(id, name))
    db.close()
