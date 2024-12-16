import sqlite3

def getconnection():
    con=sqlite3.connect('base.db')
