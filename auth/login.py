from util.validations import username_validation, password_validation


def login():
    is_valid = False
    username = ""
    message = ""
    user = None

    while not is_valid:
        print(message)
        username = str(input("\nUsername: "))

        is_valid, message, user = username_validation(username)

    if is_valid:
        is_valid = False

        while not is_valid:
            print(message)
            password = str(input("\nPassword: "))

            is_valid, message = password_validation(user, password)

        if is_valid:
            print("welcome back " + username)
            # TODO: Check Privileges and continue submenu work
