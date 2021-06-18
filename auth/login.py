from util.validations import username_validation, password_validation
from user import UserManager

def login():
    print("I am in login")
    is_valid = False
    username = ""
    message = ""
    user = None

    while not is_valid:
        print(message)
        print("I am in is_valid")
        username = str(input("\nUsername: "))

        is_valid, message, user = username_validation(username)

    if is_valid:
        is_valid = False

        while not is_valid:
            print(message)
            password = str(input("\nPassword: "))

            is_valid, message = password_validation(user, password)

        if is_valid:
            print("Is valid")
            
            # DataBaseManager().query("users", username)
            theUser = UserManager().find_user_by_username(username)
            print(theUser.type)
            # if theUser.type == 0
            if theUser.type == "0":
                print("Welcome back Normie: " + username)

            if theUser.type == "2":
                print("Welcome back ADMIN: " + username)
            
            # TODO: Check Privileges and continue submenu work
            
        
