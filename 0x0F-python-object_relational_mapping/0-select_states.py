#!/usr/bin/python3
'''
Get all states
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", port=3306, charset="utf8",
                           user=argv[1], passwd=argv[2], db=argv[3])
    mycur = connection.cursor()
    mycur.execute("SELECT * FROM states ORDER BY states.id ASC")
    rows = mycur.fetchall()
    for row in rows:
        print(row)
    mycur.close()
    connection.close()
Footer
