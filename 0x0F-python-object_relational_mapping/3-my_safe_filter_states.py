#!/usr/bin/python3
"""usage: use the SQL injection"""

import MySQLdb
from sys import argv

if __name__=="__main__":
    username, password, database = argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
            user="username", passwd="password", db="database")
    cur = conn.cursor()
    sql = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    cur.execute(sql, ('%' + argv[4] + '%',))
    query = cur.fetchall()
    for row in query:
        print(row)
    cur.close()
    conn.close()
