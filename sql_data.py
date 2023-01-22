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
#          )""")

#Inserts a new user into the SQl database
def insert_user(user):
    with conn:
        c.execute("INSERT INTO users VALUES (:username, :password, :email)", {'username': user.name, 'password': user.password, 'email': user.email})

#Looks through the database to find users whose usernames = name
def get_users_by_name(name):
    c.execute("SELECT * FROM users WHERE username=:username", {'username': name})
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
                  {'username': user.name, 'email': user.email, 'password': password})
#Deletes users whose usernames and passwords are equal to the user compared to.
def remove_user(user):
    with conn:
        c.execute("DELETE from users WHERE username = :username AND password = :password",{'username':user.name, 'password': user.password})

#incomplete password and username checker
def check_Credentials(name, password):
    user = get_users_by_name(name)
    if user.getName() == name or user.getPassword() == password:
        return True
    return False
<<<<<<< Updated upstream
=======

insert_user(Users(input("Enter Your Full Name: "),input("Enter Your Email: "), input("Create Your Password: ")))
print("You have successfully created a new account")
>>>>>>> Stashed changes
