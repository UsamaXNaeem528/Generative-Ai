########################################################################################
###########################* STRINGS IN PYTHON Exercise *###############################
########################################################################################

#! 1. Create 3 variables to store street, city and country, now create address variable to store 
#! entire address. Use two ways of creating this variable, one using + operator and the other using f-string.
#! Now Print the address in such a way that the street, city and country prints in a separate line.

street = "NYC street no. 5"
city = "New York"
country = "United States of America"
address = street + "\n" + city + "\n" + country
print(address)

#! 2. Create a variable to store the string "Earth revolves around the sun".
#! Print "revolves" using slice operator.
#! Print "sun" using negative index.

earth_sun = "Earth revolves around the sun"
print(earth_sun[6:14])
print(earth_sun[-3:])

#! 3. Create two variables to store how many fruits and vegetables you eat in a day.
#! Now Print "I eat x veggies and y fruits daily" where x and y presents vegetables
#! and fruits that you eat everyday. Use python f string for this.

fruits = "4"
vegetables = "6"
print(f'I eat {vegetables} veggies and {fruits} fruits daily.')

#!4. I have a string variable called s='maine 200 banana khaye'.
#! This of course is a wrong statement, the correct statement is 'maine 10 samosa khaye'.
#! Replace incorrect words in original strong with new ones and print the new string.
#! Also try to do this in one line.

s='maine 200 banana khaye'
s = s.replace('200 banana', '10 samosa')
print(s)