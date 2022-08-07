#!/usr/bin/python3
"""comment aaa"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect('localhost', argv[1], argv[2], argv[3], 3306)
    cursor = db.cursor()
    sql = "SELECT cities.name FROM cities INNER JOIN states\
        ON cities.state_id = states.id WHERE states.name = %s"
    cursor.execute(sql, (argv[4],))
    res = cursor.fetchall()
    if len(res) == 0:
        print('')
    for i in range(len(res)):
        if i != (len(res) - 1):
            print("{}, ".format(res[i][0]), end="")
        else:
            print(res[i][0])
    db.close()
