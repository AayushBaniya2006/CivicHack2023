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
    def userName(self):
        return '{}'.format(self.name)

    @property
    def __repr__(self):
        return "Employee('{}','{}', '{}')".format(self.name, self.password, self.email)
    

