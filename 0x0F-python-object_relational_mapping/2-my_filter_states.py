#!/usr/bin/python3
"""usage: search for the value who matches with argument"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT * FROM states
            WHERE name LIKE BINARY '{}'
            ORDER BY id ASC".format(argv[4]))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
