#!/usr/bin/python3
"""usage: use the SQL injection"""

import MySQLdb
from sys import argv

if __name__=="__main__":
    conn = MySQLdb.connect(
            host="localhost", port=3306, charset="utf8",
            user=argv[1], passwd=argv[2], db=argv[3]
    )
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(sql, ('%' + argv[4] + '%',))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
