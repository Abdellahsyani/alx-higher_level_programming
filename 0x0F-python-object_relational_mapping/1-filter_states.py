#!/usr/bin/python3
"""list all states that's start with n capital"""

import MySQLdb
import sys

if __name__=="__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[0], passwd=argv[1], db="hbtn_0e_0_usa")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states hbtn_0e_0_usa
            WHERE UPPER(name) LIKE N%
            ORDER BY id ASC")
    query = cur.fetchall()
    for row in query:
        print(row)

    cur.close()
    conn.close()
