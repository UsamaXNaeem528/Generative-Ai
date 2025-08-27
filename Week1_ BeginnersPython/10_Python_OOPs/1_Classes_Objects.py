'''============================Python Classes/Objects============================='''
'''
Python is an object oriented programming language.
In Python, everything you use or create — numbers, strings, functions, even classes — is actually an object of some class (or type). That includes things you don’t usually think of as objects, like:
int (e.g., 5)
str (e.g., "hello")
list (e.g., [1, 2, 3])
function
class
None
'''

'''===================================Creating  a Class==============================='''
#*Example 1:
class Student:     #====> class
    name = 'Usama'

s1 = Student()     #====> 1st obejct of class student
print(s1.name)
s2 = Student()      #====> 2nd object of class student
print(s2.name)


'''=================================Constructors in Classes============================'''
#* Constructor runs/class automatically when the object of class is being intiaited or made.
#* Two types of constructors in class
#* i. default constructor(dont need to write until you don't need), 
#* ii. parametermized constructor def __init__(self, other parameters..) 
#* iii. if we made it we must have to pass the parameter in class object initialization. 
#* compulsory===>(in this "self" is the reference of object)

class Car:
    #default constructor no need to write(i write it for understanding)
    # def __init__(self):
    #     print("I am a default constructor of Class Car")
    
    #parameterized contructor of class
    def __init__(self, brand, name, color):
        self.brand = brand
        self.name = name
        self.color = color

car1 = Car('corolla','prius','black')
print(car1.brand, car1.name, car1.color)

'''========================Class Attributes aand Instance Attributes======================='''
#* In class data is the attributes like properties.
#*attributes are the variables in classes
#* ✅ Instance or object Attribute:
#* Har object (yaani instance) ke apne alag attributes hotay hain.
#* Ye attributes __init__ method ke andar set kiye jaate hain.
#* Har object ka apna value hota hai, aur ye doosray object se independent hota hai.

#* ✅ Class Attribute:
#* Ye attribute class level par hota hai.
#* Sabhi objects (instances) isay share karte hain.
#* Agar aap class attribute ko change karte hain class ke level par, to sab objects mein wo reflect hota hai (agar unhone overwrite nahi kiya ho).

class Student:
    college_name = "Atchison College" # --> class attribute
    
    def __init__(self, name, marks):
        self.name = name    # --> Instance attribute
        self.marks = marks
        print("Adding New Student into the database")

#accesing instance attribute
s1 = Student('Harry', '90')
print(s1.name, s1.marks)
s2 = Student('John','50')
print(s2.name, s2.marks)

# Student.college_name = 'PGC'  # we over write the class level attribute

#accessing class attrbite
print(Student.college_name)

#!Imp=>Preference of Instance attribute is greater than class attribute in case name same attrbute variable.

'''=================================Methods in Classes============================'''
#* Methods are the functions in Class.
#* we can access it using instance or object
#* In method we must have to pass parameter 'self' ==> def hello(self):  other wise you got error

class Student:
    
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def greet(self):
        print("Hello Student", self.name)
        
s1 = Student('Usama','100')
s1.greet()

# '''=================================Static Methods in Classes============================'''
# #* Python mein static method ek aisa method hota hai jo na to class instance (self) ka use karta hai,
# #* na hi class (cls) ka. Iska matlab ye method kisi object-specific ya class-specific data ko access
# #* nahi karta.
# #* matlab static method wab use karna chahiye jab hame class ka attributes or members ki class ma 
# #* zaroorat nahi?"
# #* ye class ma is liye likhe jaate ha, take code organize rahe.

class Temprature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celcius(f):
        return (f - 32) * 5/9

t1 = Temprature()
print(t1.celsius_to_fahrenheit(12))
print(t1.fahrenheit_to_celcius(12))
