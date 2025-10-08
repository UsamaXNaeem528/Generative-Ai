#Polymorphism : means same name functions with the different working and behaviour in different clases
# Poly (many) + Morph (forms)

#===================================================
#1. Simple Polymorphism with objects and functions #
#===================================================
class Car:
    def drive(self):
        return "Car is driving"

class Ship:
    def drive(self):
        return "Ship is drive on sea"
class Train:
    def drive(self):
        return "Train is start driving on rails"
        
#now see the magic of polyMorpism
vehicles = [Car(), Ship(), Train()]
for i in vehicles:
    print(i.drive())
    
#=====================================================
#              Run Time Polymorphism                 #
#2. Polymorphism with inheritence (method overriding)#             
#=====================================================
# run time polymorphism : when a child class When a child class defines a method that already exists in the parent class,
# it overrides the parent’s behavior.

class Bike:
    def tyres(self):
        return "Bike has 2 typres"

class Cg125:
    def tyres(self):
        return "Cg 125 has 2 tyres"

class Ybr125:
    def tyres(self):
        return "Yahama YBR has 2 tyres"

b1 = Bike()
c1 = Cg125()
y1 = Ybr125()

b1.tyres()
c1.tyres()
c1.tyres()



















































    




        
        