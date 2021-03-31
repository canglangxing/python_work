class User:
    """docstring for User"""
    def __init__(self, first_name, last_name, age, location):
        self.f_name = first_name
        self.l_name = last_name
        self.age = age
        self.location = location

    def describe_user(self):
        print("\nHere is some information about the user:")
        print(f"Name: {self.f_name} {self.l_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")

    def greet_user(self):
        print(f"Hello, {self.f_name} {self.l_name}")

# class Privileges:
#     """docstring for ClassName"""
#     def __init__(self):
#         self.privileges = ['can add post', 'can delete post', 'can ban user']

#     def show_privileges(self):
#         print("As an administrator, you have some privileges:")
#         for priviliege in self.privileges:
#             print(priviliege.title())        

# class Admin(User):
#     def __init__(self, first_name, last_name, age, location):
#         super().__init__(first_name, last_name, age, location)
#         self.privileges = Privileges()


# Zhang = Admin('Zhang', 'Fuhong', 26, 'Shanghai')
# Zhang.privileges.show_privileges()