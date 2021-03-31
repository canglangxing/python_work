class User(object):
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

user1 = User('Mary', 'Jane', '24', 'New York')
user1.describe_user()
user1.greet_user()

user1 = User('Zhang', 'Fan', '16', 'Shanghai')
user1.describe_user()
user1.greet_user()

user1 = User('Alex', 'Hillton', '50', 'Berlin')
user1.describe_user()
user1.greet_user()