#!/usr/bin/python3

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_capacity(self):
        print(super().seating_capacity(50))
    

b = Bus("bus1", 80, 60)
b.seating_capacity()
