# a. Duck typing is another way to achieve polymorphism besides Inheritance.
#   It is a concept in programming based on the phrase 
#   "If it looks like a duck and quacks like a duck, it must be a duck."
#   It determines an object's suitability by its available methods and properties rather than its class type 
#   
# b. It needed a move() method matching the one called inside the loop or function.   

class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()

start_trip(car)
start_trip(boat)
start_trip(drone)

#  start_trip() works with different objects (Car, Boat, Drone) 
# through a shared interface (move()) without requiring inheritance 
# or explicit type checks. 