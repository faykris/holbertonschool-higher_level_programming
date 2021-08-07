#!/usr/bin/python3
"""
1. Filter states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         password=password, database=database,
                         charset="utf8")
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
