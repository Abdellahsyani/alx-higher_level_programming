#!/usr/bin/python3
"""usage: list all cities in database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], database=argv[3]
    )

    cur = conn.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name\
            FROM cities\
            JOIN states ON cities.state_id = states.id\
            ORDER BY cities.id ASC""")
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    conn.close()
