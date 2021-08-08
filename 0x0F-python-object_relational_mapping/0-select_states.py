#!/usr/bin/python3

'''
lists all states from the database hbtn_0e_0_usa
'''

import MySQLdb as sql
import sys

if __name__ == '__main__':
    '''
    take 3 arguments: <<mysql username>>, <<mysql password>> and
    <<database name>>
    '''
    conection = sql.connect(host='localhost', port=3306,
                            user=sys.argv[1], passwd=sys.argv[2],
                            db=sys.argv[3], charset='utf8')
    cursor = conection.cursor()
    cursor.execute('SELECT * FROM states')
    rows = cursor.fetchall()
    for i in rows:
        print(i)
