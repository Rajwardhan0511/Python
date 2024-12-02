#!/usr/bin/python3

class Vehicle:
    def __init__(self,max_speed, milages):
        self.max_speed = max_speed
        self.milages = milages

    def show(self):
        print(f"Max Speed: {self.max_speed}, Milage: {self.milages}")

e = Vehicle(400,5)
e.show()
