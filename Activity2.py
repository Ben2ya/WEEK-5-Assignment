class Vehicle:
    def move(self):
        pass  # abstract action, to be defined by subclasses

class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying ")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Using Polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()
