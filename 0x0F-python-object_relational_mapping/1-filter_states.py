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
    c = dbase.connect(user=arg1, passwd=arg2, db=arg3, host=my_host, port=3306)
    q = c.cursor()
    q.execute("SELECT id, name FROM states ORDER BY id ASC")
    rows = q.fetchall()
    for row in rows:
        if row[1][0] == "N":
            print(row)
