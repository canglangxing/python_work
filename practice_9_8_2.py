from practice_9_8_1 import User

class Privileges:
    """docstring for ClassName"""
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print("As an administrator, you have some privileges:")
        for priviliege in self.privileges:
            print(priviliege.title())        

class Admin(User):
    def __init__(self, first_name, last_name, age, location):
        super().__init__(first_name, last_name, age, location)
        self.privileges = Privileges()