#!/usr/bin/python3
"""usage: search for the value who matches with argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3])
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
