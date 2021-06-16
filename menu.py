# def main():
#     menu()

# Menu File
from auth.login import login


def menu():
    print("----- Welcome to SCRS -----")
    print("[1] Sign in")
    print("[2] Sign up")
    print("[3] Guest Session")
    print("[0] Exit")


menu()
option = int(input("\nSelect an Option: "))

while option != 0:
    if option == 1:
        print("option signin")
        login()
    elif option == 2:
        # do option two signup
        print("option signup")
    elif option == 3:
        # do option three guest
        print("option guest")
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
