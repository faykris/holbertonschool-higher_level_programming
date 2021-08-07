#!/usr/bin/python3
"""
3. SQL Injection...
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states
                   WHERE name = %s ORDER BY id ASC""", (sys.argv[4],))
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()
