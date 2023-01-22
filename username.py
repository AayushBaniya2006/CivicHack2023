#Creates the user class
class Users:
    
    def __init__(self, name, password, email):
        self.name = name
        self.password = password
        self.email = email
    
    @property
    def profileInfo(self):
        return '{}','{}'.format(self.name, self.email)
    
    @property
    def getName(self):
        return '{}'.format(self.name)
    
    @property
    def getPassword(self):
        return '{}'.format(self.password)

    @property
    def __repr__(self):
        return "Employee('{}','{}', '{}')".format(self.name, self.password, self.email)
    
