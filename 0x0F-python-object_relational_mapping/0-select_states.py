#!/usr/bin/python3
"""
Task 0 - Write a script that lists all states from the database hbtn_0e_0_usa
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(user=argv[0],
                         passwd='root',
                         db=argv[2]
                         )
    mycur = db.cursor()
    mycur.execute("SELECT * FROM states ORDER BY state.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
        """closing the cursor"""
    cur.close()
    """closing the database"""
    db.close()
