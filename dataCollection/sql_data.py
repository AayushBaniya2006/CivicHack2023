import sqlite3
from username import Users
#variable that connects to SQL database
conn = sqlite3.connect('users.db')

#cursor - allows from running of SQL commands
c = conn.cursor()

#6 quotations basically just allow you to make 1 string across multiple lines
#Creates table-> Only needs to be run once.
#c.execute("""CREATE TABLE users (
#            username TEXT,
#            password TEXT,
#            email TEXT
#            )""")

def insert_user(user):
    with conn:
        c.execute("INSERT INTO users VALUES (:username, :password : email)", {'username': user.username, 'password': user.password, 'email': user.email})

def get_users_by_name(name):
    c.execute("SELECT * FROM employees WHERE username=:username", {'username': name})
    return c.fetchall()
    
def update_username(user, name):
        with conn:
            c.execute("""UPDATE users SET username = :username
                  WHERE password = :password AND email = :email""",
                  {'password': user.password, 'email': user.email, 'username': name})
        
def update_userpassword(user, password):
    with conn:
        c.execute("""UPDATE users SET password = :password
                  WHERE username = :username AND email = :email""",
                  {'username': user.username, 'email': user.email, 'username': password})

def remove_user(user):
    with conn:
        c.execute("DELETE from users WHERE username = :username AND password = :password",
                  {'username':user.first, 'password': user.password})

#incomplete password and username checker
