#!/usr/bin/python3
""" ensure the file is executed"""
if __name__ == '__main__':
""" importing modules to be used """

import MySQLdb
import sys

""" conect to the the database """

db = MySQLdb.connect(host='localhost', port=3306,
        user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

""" use cursor function to querry the database """
mycursor = db.cursor()
mycursor.conect("SELECT * FROM  states ORDERED BY states.id ASC;")
rows = cur.fetchall()
    for row in rows:
        print(row)
