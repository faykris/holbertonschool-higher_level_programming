#!/usr/bin/python3
"""
4. Cities by states
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], database=sys.argv[3])
    cursor = db.cursor()
    sql = """SELECT cities.id, cities.name, states.name FROM states
             INNER JOIN cities ON states.id = cities.state_id
             ORDER BY cities.id ASC"""
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        print(row)
    db.close()
