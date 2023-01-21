import sqlite3
from username import Users
#variable that connects to SQL database
conn = sqlite3.connect('users.db')

#cursor - allows from running of SQL commands
c = conn.cursor()

#6 quotations basically just allow you to make 1 string across multiple lines
#Creates table-> Only needs to be run once.
#c.execute("""CREATE TABLE users (
 #           username TEXT,
 #           password TEXT,
 #           email TEXT
#            )""")

#Inserts data into the table
c.execute("INSERT INTO users VALUES ('Mary', 'IAmTheDanger', 'lock&key@gmail.com')")

#Pulls data from SQL database
c.execute("SELECT * from users")

#Fetches one row from the table
print(c.fetchone())
#Fetches all rows from the table
print(c.fetchall())

user_1 = Users('JackStauber', 'PokingCars', 'placeholder')
c.execute("INSERT INTO users VALUES (?, ?, ?)", (user_1.name, user_1.password, user_1.email))
#commits current transaction -> Puts data in database
conn.commit()

#closes the database
conn.close()