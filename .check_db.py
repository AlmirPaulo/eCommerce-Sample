#! /usr/bin/env python3
import sqlite3

conn = sqlite3.connect('ecommerce/db.sqlite3')
c = conn.cursor()
table = 'user' 

c.execute('SELECT * FROM '+table)
data = c.fetchall()
print(data)


#for row in data:
 #   print(row)
