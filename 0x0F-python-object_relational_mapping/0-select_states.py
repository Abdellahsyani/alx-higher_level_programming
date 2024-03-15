#!/usr/bin/python3
"""List all states inside the database"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], database=argv[3]
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
