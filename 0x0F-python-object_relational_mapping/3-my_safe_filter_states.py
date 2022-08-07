#!/usr/bin/python3
"""comment aaa"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], 3306)
    cursor = db.cursor()
    sql = "SELECT * FROM states WHERE name = %s"
    cursor.execute(sql, (argv[4],))
    res = cursor.fetchall()
    for row in res:
        if row[1] == argv[4]:
            print(row)
    db.close()
