#creating a new user
from user import UserManager
from util.validations import username_signup

def Signup():
    # is_valid = False
    # username = ""
    # password = ""
    # message = ""
    # user = None

    print("I am in signup.py")
    username = input("Please enter a username: ")
    password = input("Please enter a password: ")

    UserManager().create_user(username, password)


    