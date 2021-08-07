#!/usr/bin/python3
"""
1. Filter states
"""
import sys
import MySQLdb


def realize_query(user, password, database):
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


if __name__ == "__main__":
    realize_query(sys.argv[1], sys.argv[2], sys.argv[3])
