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

#Hopefully, a method that removes usernames the name in the removeUser(name) refers to the original username that a user wishes to change
def removeUser(name):
    print('Enter the your new name')
    x = input()
    theUser = get_users_by_name(name)
    remove_user(theUser, x)

def changeName(name):
    theUser = get_users_by_name(name)
    (theUser)

#Inserts a new user into the SQl database
def insert_user(user):
    with conn:
        c.execute("INSERT INTO users VALUES (:username, :password : email)", {'username': user.username, 'password': user.password, 'email': user.email})

#Looks through the database to find users whose usernames = name
def get_users_by_name(name):
    c.execute("SELECT * FROM employees WHERE username=:username", {'username': name})
    return c.fetchall()
    
#Changes username
def update_username(user, name):
        with conn:
            c.execute("""UPDATE users SET username = :username
                  WHERE password = :password AND email = :email""",
                  {'password': user.password, 'email': user.email, 'username': name})
#Similar to username -> Changes password
def update_userpassword(user, password):
    with conn:
        c.execute("""UPDATE users SET password = :password
                  WHERE username = :username AND email = :email""",
                  {'username': user.username, 'email': user.email, 'username': password})
#Deletes users whose usernames and passwords are equal to the user compared to.
def remove_user(user):
    with conn:
        c.execute("DELETE from users WHERE username = :username AND password = :password",
                  {'username':user.first, 'password': user.password})

#incomplete password and username checker
def check_Credentials(name, password):
    user = get_users_by_name(name)
    if user.getName() == name or user.getPassword() == password:
        return True
    return False