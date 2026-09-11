# Abstraction example in Python
from abc import ABC, abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
class Car(Vehicle):
    def start(self):
        print("Car starts with a key")
class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button")
car =Car()
bike = Bike()
vehicle = Vehicle() # This will raise an error because Vehicle is an abstract class and cannot be instantiated
car.start()
bike.start()