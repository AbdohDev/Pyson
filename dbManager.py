class DataBaseManager:

    def create_record(self):
        pass

    # with open("users.txt", "w") as fh:
    #     fh.write("abdoh")

    with open("db/users.txt", "a") as fh:
        fh.write("a")

    def read_record(self, table):
        with open("db/" + table + ".txt", "r") as fh:
            line = fh.readline()
            print(line)

    def update_record(self):
        pass

    def delete_record(self):
        pass
