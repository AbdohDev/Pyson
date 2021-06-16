from user import UserManager, User


def username_validation(username):
    if str(username).__len__() == 0:
        return False, "Please enter the valid username", None

    user = UserManager().find_user_by_username(str(username).strip())
    if user is None:
        return False, "User does not exist", None

    return True, "", user


def password_validation(user, password):
    if str(password).__len__() <= 4:
        return False, "Password Length should be at least 5 characters"

    # TODO: you can add here any other validation for password, such as containing at
    #  least one letter or whatever you want

    if user.password != str(password).strip():
        return False, "Enter a correct password"

    return True, ""
