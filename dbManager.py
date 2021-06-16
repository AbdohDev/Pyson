import os


class DataBaseManager:

    def create_record(self):
        pass

    # with open("users.txt", "w") as fh:
    #     fh.write("abdoh")

    with open("db/users.txt", "a") as fh:
        fh.write("a")

    def read_record(self, table):
        with open(os.path.join("db", table + ".txt"), "r") as fh:
            line = fh.readline()

            return line

    def read_all(self, table):
        all_records = []

        with open(os.path.join("db", table + ".txt"), "r") as fh:
            line = fh.readline()
            all_records.append(line)

        return all_records

    # TODO: This function may be updated if the database files become more complex
    def query(self, table, condition):
        with open(os.path.join("db", table + ".txt"), "r") as fh:
            line = fh.readline()
            if str(line).strip() == str(condition).strip():
                return line

        return None

    def update_record(self):
        pass

    def delete_record(self):
        pass
