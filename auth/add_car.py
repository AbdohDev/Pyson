from cars import CarManager


def add_car():
    print("I am in add_car")
    company = input("Enter a car company: ")
    model = input("Enter a car model: ")
    year = input("Enter the car year: ")
    
    CarManager().add_car(company, model, year)
