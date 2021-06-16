# printing the starting line  
import dbManager
import menu
dbMan = dbManager.DataBaseManager()
menu.menu()

dbMan.read_record("users")

dbMan.read_record("cars")


dbManager.DataBaseManager().read_record(table="user")


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