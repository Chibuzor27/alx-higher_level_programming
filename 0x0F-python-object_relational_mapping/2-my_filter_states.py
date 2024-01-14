#!/usr/bin/python3
""" Filter states starting with N """


import MySQLdb
import sys

if __name__ == "__main__":
    con = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3])
    cursor = con.cursor()
    cursor.execute('SELECT * FROM states \
        WHERE name LIKE "{}" ORDER BY states.id ASC'.format(sys.argv[4]))
    records = cursor.fetchall()

    for row in records:
        print(row)

    cursor.close()
    con.close()
