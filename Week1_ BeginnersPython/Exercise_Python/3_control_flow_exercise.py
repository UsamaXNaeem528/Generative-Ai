# Question 1
'''
Using following list of cities per country,
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

i.Write a program that asks user to enter a city name and it should tell which country the city belongs to

ii.Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and dhaka it should print 
"They don't belong to same country"
'''
india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

city = str.lower(input("Enter a city name : "))
country = str.lower(input("Which country the city belongs to : "))
print(f"City {city} belongs to Country {country}")

#=============================

first_city = str(input(f'Enter 1st City : '))
second_city = str(input(f'Enter 2nd City : '))

# Check if both cities belong to the same country
if(first_city in india and second_city in india):
    print('Both cities are in India')
elif(first_city in pakistan and second_city in pakistan):
    print('Both cities are in Pakistan')
elif(first_city in bangladesh and second_city in bangladesh):
    print('Both cities are in Bangladesh')
else:
    print('They don\'t belong to same country')
    
    
# Question 2
'''
Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80 to 100.
Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal
'''
sugar = int(input(f'Enter your sugar level : '))
if(sugar<70):
    print("Your sugar level is too low! (Hypoglycemia)")
elif(sugar>=70 or sugar<=130):
    print("Your Sugar level is normal")
elif(sugar>130):
    print("Your sugar level is high! (Hyperglycemia)")
    


