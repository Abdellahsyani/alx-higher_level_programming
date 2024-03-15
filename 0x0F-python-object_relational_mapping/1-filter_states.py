#!/usr/bin/python3
"""list all states that's start with n capital"""

import MySQLdb

conn = MySQLdb.connect(
        host="localhost", port=3306, charset="utf8",
        user="username", passwd="password", db="hbtn_0e_0_usa")
cur = conn.cursor()
cur.execute("SELECT * FROM states hbtn_0e_0_usa
        WHERE UPPER(name) LIKE N%
        BY states.id ASC")
query = cur.fetchall()
for row in query:
    print(query)

conn.close()
cur.close()
