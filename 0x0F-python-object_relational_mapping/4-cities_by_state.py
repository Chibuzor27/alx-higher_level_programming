#!/usr/bin/python3
""" List cities """


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
    cursor.execute('SELECT cities.id, cities.name, states.name \
        FROM states JOIN cities ON states.id = cities.state_id \
        ORDER BY cities.id ASC')
    records = cursor.fetchall()

    for row in records:
        print(row)

    cursor.close()
    con.close()
