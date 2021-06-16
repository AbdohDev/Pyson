from dbManager import DataBaseManager


# cars database
class Car:
    def __init__(self, carplate, company, model, year, cost):
        self.carplate = carplate
        self.company = company
        self.model = model
        self.year = year
        self.cost = cost
        

class CarManager:
    def __init__(self):
        self.fill_all_cars()
        
    cars = []
    
    def fill_car(self, car_record):
        car_data = str(car_record).split(',')
        
        car = Car(cost=car_data[1], company=car_data[2], carplate=car_data[0], model=car_data[1], year=car_data[3])

        return car
    
    def fill_all_cars(self):
        if self.cars.__len__() > 0:
            return

        cars_records = DataBaseManager().read_all('cars')

        for record in cars_records:
            self.cars.append(self.fill_car(record))

    def find_car_by_carplate(self, carplate):
        if self.cars.__len__() == 0:
            return None
            
        for car in self.cars:
            if car.carplate == carplate:
                return car

        return None
        
    def add_car(self, company, model, year):
        DataBaseManager().create_record("cars",company +"," + model + "," + year)