#!/usr/bin/python3
"""
4. Cities by states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    sql = """SELECT cities.id, cities.name, states.name FROM states
             INNER JOIN cities ON states.id = cities.state_id
             ORDER BY cities.id ASC"""
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        id = row[0]
        city = row[1]
        state = row[2]
        print("({}: '{}', '{}')".format(id, city, state))
    db.close()
