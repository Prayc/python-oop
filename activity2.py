# Parent Class
class Vehicle:
    def move(self):
        pass  # To be overridden by child classes


# Child Class 1
class Car(Vehicle):
    def move(self):
        return "The car is driving on the road 🚗"


# Child Class 2
class Plane(Vehicle):
    def move(self):
        return "The plane is flying in the sky ✈️"


# Child Class 3
class Boat(Vehicle):
    def move(self):
        return "The boat is sailing on the water 🚤"


# Demonstration of Polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())
