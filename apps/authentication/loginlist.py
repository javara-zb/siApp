import sqlite3 

conn = sqlite3.connect('db.sqlite3')

c = conn.cursor()

c.execute('SELECT * FROM sqlite_schema') 
# retrieve all the data from the users table 
users = c.fetchall() 


print(users)