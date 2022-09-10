#!/usr/bin/python3
'''This module selects all states from a state table'''
import MySQLdb as dbase
import sys

if __name__ == "__main__":
    args = sys.argv
    arg1 = args[1]
    arg2 = args[2]
    arg3 = args[3]
    my_host = 'localhost'
    try:
        c = dbase.connect(user=arg1, passwd=arg2, db=arg3, host=my_host, port=3306)
    except dbase.Error:
        exit()
    try:
        q = c.cursor()
    except dbase.Error:
        exit()
    col1, table = "cities.id", "cities"
    try:
        q.execute("""SELECT * FROM {}
                ORDER BY {} ASC""".format(table, col1))
        rows = q.fetchall()
    except dbase.Error:
        exit()
    for row in rows:
        print(row)
