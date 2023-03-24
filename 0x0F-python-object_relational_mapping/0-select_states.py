#!/usr/bin/python3
"""
   script that lists all states from the database hbtn_0e_0_usa
   @author: Chibuokem Obiegbulem
"""
import MySQLdb
import sys


if __name__ = '__main__':

    username, password, database = sys.argv[1:]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY id ASC")

    states = cur.fetchall()

    for state in states:
        print(state)

    cur.close()
    db.close()
