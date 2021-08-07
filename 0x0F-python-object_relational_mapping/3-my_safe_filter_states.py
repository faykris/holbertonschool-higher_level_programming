#!/usr/bin/python3
"""
3. SQL Injection...
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                   WHERE name = %s ORDER BY id ASC""", (sys.argv[4],))
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        name = row[1]
        print("({}: '{}')".format(id, name))
    db.close()
