from dbManager import DataBaseManager


# Users database
class User:
    def __init__(self, username, password, id, name, type):
        self.username = username
        self.password = password
        self.id = id
        self.name = name
        self.type = type


class UserManager:
    def __init__(self):
        self.fill_all_users()

    users = []

    def fill_user(self, user_record):
        user_data = str(user_record).split(',')

        user = User(username=user_data[1], password=user_data[2], id=user_data[0], name=user_data[1], type=user_data[3])

        return user

    def fill_all_users(self):
        if self.users.__len__() > 0:
            return

        users_records = DataBaseManager().read_all('users')

        for record in users_records:
            self.users.append(self.fill_user(record))

    def find_user_by_username(self, username):
        if self.users.__len__() == 0:
            return None

        for user in self.users:
            if user.username == username:
                return user

        return None

    def create_user(self, username, password):
        DataBaseManager().create_record("users",username +"," + password)