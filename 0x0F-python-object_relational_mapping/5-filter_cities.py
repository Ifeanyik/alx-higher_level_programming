#!/usr/bin/python3
'''This module selects all states from a state table'''
import MySQLdb as dbase
import sys

if __name__ == "__main__":
    args = sys.argv
    arg1 = args[1]
    arg2 = args[2]
    arg3 = args[3]
    state = args[4]
    my_host = 'localhost'
    count = 0
    safe_string = ''
    while state[count] != ";":
        safe_string += state[count]
        count += 1
        if count == len(state):
            break
    c = dbase.connect(user=arg1, passwd=arg2, db=arg3, host=my_host, port=3306)
    q = c.cursor()
    cn = "cities.name"
    csid = "cities.state_id"
    sid = "states.id"
    sn = "states.name"
    q.execute("""SELECT {}, {}, {}, {} FROM cities, states
            WHERE states.name = '{}'
            AND {} = {}""".format(cn, csid, sid, sn, safe_string, csid, sid))
    rows = q.fetchall()
    count = 0
    for row in rows:
        if count == len(rows) - 1:
            print(row[0])
            break
        print("{}, ".format(row[0]), end="")
        count += 1
