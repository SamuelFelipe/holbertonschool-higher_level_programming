#!/usr/bin/python3

'''
takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument
'''

import MySQLdb as sql
import sys


def prevent(unsafe):
    safe = ''

    for i in unsafe:
        if i in ['\'', '\\']:
            safe += '\\' + i
        else:
            safe += i

    return safe


if __name__ == '__main__':
    '''
    take 4 arguments: mysql username, mysql password,
    database name and state name searched
    '''
    conection = sql.connect(host='localhost', port=3306,
                            user=sys.argv[1], passwd=sys.argv[2],
                            db=sys.argv[3], charset='utf8')
    cursor = conection.cursor()
    args = prevent(sys.argv[4])
    cursor.execute('SELECT * FROM states WHERE name\
                    = \'{}\''.format(args))
    rows = cursor.fetchall()
    for i in rows:
        print(i)
