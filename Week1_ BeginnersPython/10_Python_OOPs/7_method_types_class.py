# '''=================================Static Methods in Classes============================'''
# A static method is a function inside a class that:
# Doesn’t use self (no access to the object)
# Doesn’t use cls (no access to the class)
# Acts like a normal function, but is kept inside the class for organization

class Temprature:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celcius(f):
        return (f - 32) * 5/9

print(Temprature.celsius_to_fahrenheit(12))
print(Temprature.fahrenheit_to_celcius(12))

# '''=================================Class Methods============================'''
#means changing a class level attributes  --> using cls
"""
Class methods bhi class ke andar define hote hain, lekin unka pehla parameter cls hota hai, 
jo class ko refer karta hai — na ke object ko. Inko banane ke liye @classmethod decorator lagana
padta hai. Class methods ka use tab hota hai jab hume class-level data (jaise class variables) ko
access ya modify karna ho, ya alternate constructor banana ho.
"""

class Car:
    total_cars = 0

    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model
        Car.total_cars += 1   # is ma class ka name sa ham na class level attribute ko access kiya ha
    
    @classmethod
    def get_total_cars(cls):          # cls ka matlab ye class ka attribute ko refer kar raha ha
        return cls.total_cars

c1 = Car('Toyota','Corolla')
c1 = Car('Toyota','Toyota Surf')
c1 = Car('Toyota','Toyota Surf')
print(f'Total Cars {Car.get_total_cars()}')   


# '''=================================Instance Methods============================'''

"""Instance methods wo normal functions hote hain jo class ke andar define kiye jaate hain,
aur unka pehla parameter self hota hai, jo current object (instance) ko refer karta hai.
self ki madad se hum instance ke attributes ko access aur modify kar sakte hain."""





        
        









        








