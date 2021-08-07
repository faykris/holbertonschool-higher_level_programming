#!/usr/bin/python3
"""
2. Filter states by user input
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""


def realize_query(user, password, database, state):
    """function that connect with mysql and runs a query"""
    db = MySQLdb.connect(host="localhost", port=3306, user=user,
                         password=password, database=database)
    cursor = db.cursor()
    cursor.execute("""SELECT * FROM states WHERE name='{}'
                      ORDER BY states.id ASC""".format(state))
    results = cursor.fetchall()
    for row in results:
        print(row)


if __name__ == "__main__":
    from sys import argv
    import MySQLdb

    realize_query(argv[1], argv[2], argv[3], argv[4])
