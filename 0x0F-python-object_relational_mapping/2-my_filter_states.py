#!/usr/bin/python3
"""
2. Filter states by user input
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    sql = """SELECT * FROM states WHERE name = '{}'
             ORDER BY states.id ASC""".format(sys.argv[4])
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()
