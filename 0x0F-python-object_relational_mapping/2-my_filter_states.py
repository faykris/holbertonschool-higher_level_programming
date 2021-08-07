#!/usr/bin/python3
"""
2. Filter states by user input
"""
import sys
import MySQLdb


def realize_query(user, password, database):
    """function that connect with mysql and runs a query"""
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         password=password, database=database,
                         charset="utf8")
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name = '{}'
                      ORDER BY states.id ASC""".format(sys.argv[4]))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    realize_query(sys.argv[1], sys.argv[2], sys.argv[3])
