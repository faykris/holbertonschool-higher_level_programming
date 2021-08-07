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
    cursor.execute("""SELECT * FROM states WHERE name = '{}'
                   ORDER BY states.id ASC;""".format(sys.argv[4]))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()
