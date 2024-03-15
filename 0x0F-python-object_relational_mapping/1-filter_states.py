#!/usr/bin/python3
"""list all states that's start with n capital"""

import MySQLdb
from sys import argv

if __name__=="__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3]
            )
    cur = conn.cursor()
    cur.execute("SELECT * FROM states hbtn_0e_0_usa
            WHERE name LIKE N%
            ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    conn.close()
