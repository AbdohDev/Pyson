# printing the starting line  
import dbManager.DataBaseManager as dbMan

# dbMan = dbManager.DataBaseManager()

dbMan.ReadRecord("users")

dbMan.ReadRecord("cars")


# dbManager.DataBaseManager.ReadRecord( table = "user")

# print("---welcome to car rent---")

# def menu():
#     print("[1] Sign in")
#     print("[2] Sign up")
#     print("[3] Guest Login")
#     print("[0] Exit")  

# menu()
# option = int(input("Enter your option: "))

# while option !=0:
#     if option == 1:
#         pass
#     elif option == 2:
#         pass
#     elif option == 3:
#         pass
#     else:
#         pass
# print()

# menu = {}
# menu['1']="Login" 
# menu['2']="Signup"
# menu['3']="Guest"
# menu['4']="Exit"
# while True: 
#   options=menu.keys()
#   options.sort()
#     for entry in (options): 
#         print (entry, menu[entry])

#     selection=raw_input("Please Select:") 
#     if selection =='1': 
#       print ("Login")
#     elif selection == '2': 
#       print ("Signup")
#     elif selection == '3':
#       print ("Guest")
#     elif selection == '4': 
#       break
#     else: 
#       print ("Unknown Option Selected!")