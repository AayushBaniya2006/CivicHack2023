#All of this is tutorial stuff atm - can be rewritten later
class Employee :
    
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    
    @property
    def email(self):
        return '{}@email.com'.format(self.name)
    
    @property
    def fullname(self):
        return '{}'.format(self.name)
    def __repr__(self):
        return "User ('{}', '{}')".format(self.name, self.email)