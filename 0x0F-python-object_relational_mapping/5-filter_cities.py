#!/usr/bin/python3
"""
5. All cities by state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.name FROM states INNER JOIN cities
                   ON states.id = cities.state_id
                   WHERE states.name = %s
                   ORDER BY cities.id ASC""", (sys.argv[4],))
    results = cursor.fetchall()
    cities = ''
    i = 0
    for row in results:
        if i != 0:
            cities += ", "
        cities += row[0]
        i += 1
    print("{}".format(cities))
    db.close()
