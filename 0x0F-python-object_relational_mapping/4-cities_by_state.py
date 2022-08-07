#!/usr/bin/python3
"""comment aaa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], 3306)
    cursor = db.cursor()
    sql = "SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON cities.state_id = states.id"
    cursor.execute(sql)
    res = cursor.fetchall()
    for row in res:
        print(row)
    db.close()
