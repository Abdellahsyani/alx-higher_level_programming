#!/usr/bin/python3
"""usage: search for the value who matches with argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username, password, database, state = argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
            user=username, passwd=password, db=database)
    cur = conn.cursor()
    state = argv[4]
    cur.execute("""SELECT * FROM states
            WHERE name == %s
            ORDER BY id ASC""", (state,))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
