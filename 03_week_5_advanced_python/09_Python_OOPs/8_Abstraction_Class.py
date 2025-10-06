# 1️⃣ What is Abstraction?

# Abstraction is a concept in programming (and OOP).
# where you hide the complex details of how something works
# and show only the necessary parts to the user.

# Think of a car:

# You drive using the steering wheel, brake, and accelerator.

# You don’t need to know how the engine combusts fuel or how the brakes are mechanically working.

# The interface (steering, pedals) is simple; the complexity is hidden.

# In programming:

# You hide the internal implementation.

# You provide a simple interface for the user.

# 2️⃣ Abstraction in Python

# In Python, abstraction is mainly achieved using:

# Abstract Classes

# Abstract Methods

# Python provides the abc module (Abstract Base Class) to create abstract classes and methods.

# 🔹 Abstract Class

# A class that cannot be instantiated directly.

# It can have abstract methods (methods without implementation) and concrete methods (methods with implementation).

# 🔹 Abstract Method

# A method declared but not implemented in the abstract class.

# Subclasses must implement it.

from abc import ABC, abstractmethod

# Abstract Class
class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        pass  # no implementation

    def fuel_info(self):
        print("All vehicles need fuel to run.")

# Subclass
class Car(Vehicle):

    def start_engine(self):
        print("Car engine started with key.")

class Bike(Vehicle):

    def start_engine(self):
        print("Bike engine started with button.")

# Usage
# car = Car()
# car.start_engine()   # Car engine started with key
# car.fuel_info()      # All vehicles need fuel to run

# bike = Bike()
# bike.start_engine()  # Bike engine started with button



# 4️⃣ Why use Abstraction?

# Hide complexity → Users interact with a simple interface.

# Prevent direct object creation → Forces subclasses to implement important methods.

# Encourage reusability → Abstract classes define a blueprint for other classes.

# Reduce code duplication → Shared methods in abstract class, unique behavior in subclasses.

# 5️⃣ When to use Abstraction?

# When you want to define a blueprint for other classes.

# When you want to enforce certain methods in subclasses.

# When you want to hide implementation details but show only essential behavior.

# Example scenarios:

# GUI frameworks: abstract Button, concrete WindowsButton and LinuxButton.

# Payment gateways: abstract PaymentMethod, concrete PayPal, CreditCard.

# Vehicle simulation: abstract Vehicle, concrete Car, Bike.