#property decorator means we can access function from class without paranthesis like attribute of class
#like class ma funciton ha
#
# def sum(self):
#   return self.a + self.b
#
# acces this func
# obj1 = Class(2,3)
# obj.sum     ==> is ma ha na paranthesis use nahi ki aik object ki tarah value de raha like read only
#====================================================================
# 🧠 Practice Question:
# Create a class called Temperature that stores temperature in Celsius but allows:
# Accessing the temperature in Fahrenheit using a property.
# Updating the Celsius temperature via a setter.
# 🔸 Requirements:
# Class: Temperature
# Private attribute: __celsius
# Constructor: __init__(self, celsius)
# @property:
# fahrenheit: returns the temperature in Fahrenheit (use formula: F = C * 9/5 + 32)
# @property:
# celsius: getter for Celsius
# @celsius.setter:
# Validates that Celsius value is not below -273.15 (absolute zero)

# 🎯 Tasks:
# Create an object with 25°C
# Print both Celsius and Fahrenheit
# Try setting Celsius to -300 (should give a warning or error)
# Update Celsius to 100 and print Fahrenheit again

class Temprature:
    def __init__(self, celcius):
        self.__celcius = celcius
        
    @property
    def fahrenhiet(self):
        Fahrenhiet = self.__celcius * 9/5 +32
        return f'{Fahrenhiet}°F' 
    
    @property
    def get_celcius(self):
        return f'{self.__celcius}°C'
    
    @get_celcius.setter
    def get_celcius(self, value):
        if (value < -273.15):
            print("Temperature can't go below absolute zero!")
        else:
            self.__celcius = value

temp1 = Temprature(25)
print(temp1.get_celcius)
print(temp1.fahrenhiet)
# temp1.get_celcius = -300
temp1.get_celcius = 100
print(temp1.fahrenhiet)


# 🧠 Practice Question 2:
# Create a class Rectangle to manage and validate width, height, and compute area.

# 🔹 Requirements:
# Private instance attributes:

# __width

# __height

# Constructor:

# Takes width and height as arguments

# Use @property and @setter for both width and height:

# Prevent negative values (if user tries to set a negative value, print a warning and ignore the update)

# Add a read-only property:

# area → returns width * height (automatically updates when width or height changes)

# 🎯 Tasks:
# Create a rectangle with width = 10, height = 5

# Print width, height, and area

# Try setting width to -3 (should give warning)

# Set height to 20 and print new area


class Rectangle:
    def __init__(self, height, width):
        self.__height = height
        self.__width = width 
          
    @property      
    def get_width(self):
        return f'Width : {self.__width}'
    
    @get_width.setter
    def get_width(self, width):
        if(width < 0):
            print("Warning : Width must be positive")
        else:
            self.__width = width
    
    @property
    def get_height(self):
        return f'Height : {self.__height}'
    
    @get_height.setter
    def get_height(self, height):
        if(height < 0):
            print("Warning : Height must be positive")
        else:
            self.__height = height

    @property
    def area_rectangle(self):
        return f'Area Of Rectangle {self.__height * self.__width}'
    
obj1 = Rectangle(10, 5)
print(obj1.get_width)
print(obj1.get_height)
print(obj1.area_rectangle)
obj1.get_width = -3
obj1.get_height = 20
print(f'New {obj1.area_rectangle}')





        



            
            
    
        
        

    
        
                      