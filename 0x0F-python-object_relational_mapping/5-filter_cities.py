#!/usr/bin/python3
""" Filter cities """


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
    cursor.execute('SELECT cities.name \
        FROM states JOIN cities ON states.id = cities.state_id \
        WHERE states.name = %s \
        ORDER BY cities.id ASC', (sys.argv[4],))
    records = cursor.fetchall()

    names = [row[0] for row in records]
    print(', '.join(names))

    cursor.close()
    con.close()
