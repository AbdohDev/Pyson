class DataBaseManager:

    def CreateRecord():
        pass

    # with open("users.txt", "w") as fh:
    #     fh.write("abdoh")



    with open("db/users.txt", "a") as fh:
        fh.write("a")
        




    def ReadRecord(self, table):
        with open("db/" + table + ".txt", "r") as fh:
            line = fh.readline()
            print (line) 


    def UpdateRecord():
        pass

    def DeleteRecord():
        pass