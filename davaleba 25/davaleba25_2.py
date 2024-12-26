class Vehicle:
    def move(self):
        pass

class Car(Vehicle):
    def move(self):
        print("The car is driving")

class Bike(Vehicle):
    def move(self):
        print("The bike is cycling")

class Truck(Vehicle):
    def move(self):
        print("The truck is hauling")

def test_vehicles(vehicles):
    for vehicle in vehicles:
        vehicle.move()
        
vehicles = [Car(), Bike(), Truck()]

test_vehicles(vehicles)