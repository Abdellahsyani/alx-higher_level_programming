#!/usr/bin/python3
"""usage: lists all cities in one state"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], database=argv[3]
    )
    cur = conn.cursor()
    sql = "SELECT cities.name, states.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id ASC"
    state = argv[4]
    cur.execute(sql, (state,))
    query_state = cur.fetchall()
    for city in query_state:
        print(city[0])
    cur.close()
    conn.close()
