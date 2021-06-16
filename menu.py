# def main():
#     menu()

# Menu File
from auth.login import login
from auth.signup import Signup
from auth.add_car import add_car

def menu():
    print("----- Welcome to SCRS -----")
    print("[1] Login")
    print("[2] Sign up")
    print("[3] Guest Session")
    print("[4] add car")
    print("[0] Exit")


menu()
option = int(input("\nSelect an Option: "))

while option != 0:
    if option == 1:
        print("I am in menu login")
        login()
    elif option == 2:
        print("I am in menu signup")
        Signup()
    elif option == 3:
        # do option three guest
        print("option guest")
        #add car funtion will be placed under Admin login
    elif option == 4:
        print("option add car")
        add_car()
    else:
        print("Thank you for using SCRS")

    # menu()
    option = int(input("\nSelect an Option: "))

print("thanks for using SCRS")
# def signin():
#     print("this is where you sign in")
# print (menu())


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
