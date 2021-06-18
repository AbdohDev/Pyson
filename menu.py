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

def admin():
    print("----- Admin Access -----")
    print("[1] Add a car")
    print("[2] Display cars")
    print("[3] Search cars")
    print("[4] Return a rented car")
    print("[0] Exit")
    
    
admin()
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

def guest():
    print("----- Guest Session -----")
    print("[1] View all cars available for rent")
    print("[2] Register an account")
    print("[0] Exit")


def user():
    print("----- User Access -----")
    print("[1] View Booking History") #then select and book a car for a specific time # then confirm payment
    print("[2] View all cars available for rent")
    print("[0] Exit")



print("thanks for using SCRS")
