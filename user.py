# Users database
class User:
    def __init__(self, username, password, id, name, type):
        self.username = username
        self.password = password
        self.id = id
        self.name = name
        self.type = type


username = input("Enter your username: ")
