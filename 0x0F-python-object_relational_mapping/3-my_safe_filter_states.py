#!/usr/bin/python3
'''This module selects all states from a state table'''
import MySQLdb as dbase
import sys

if __name__ == "__main__":
    args = sys.argv
    arg1 = args[1]
    arg2 = args[2]
    arg3 = args[3]
    user_arg = args[4]
    count, safe_string = 0, ''
    while user_arg[count] != ";":
        safe_string += user_arg[count]
        count += 1
        if count == len(user_arg):
            break
    user_arg = safe_string
    my_host = 'localhost'
    c = dbase.connect(user=arg1, passwd=arg2, db=arg3, host=my_host, port=3306)
    q = c.cursor()
    col1, col2, table = "id", "name", "states"
    q.execute("""SELECT {}, {} FROM {}
            WHERE {}='{}'
            ORDER BY {} ASC""".format(col1, col2, table, col2, user_arg, col1))
    rows = q.fetchall()
    for row in rows:
        print(row)
