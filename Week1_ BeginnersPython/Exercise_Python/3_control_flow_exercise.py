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

#===============================================================================

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
    

#===============================================================================

#Question 3:
'''
After flipping a coin 10 times you got this result,
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
Using for loop figure out how many times you got heads
'''
result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
heads = 0
for x in result:
    if(x == "heads"):
        heads += 1

print(f'After flipping coin heads come for {heads} times.')

#===============================================================================

#Question 4:
'''Print square of all numbers between 1 to 10 except even numbers'''

for i in range(1,11):
    if(i % 2 != 0):
        print(i*i)

#===============================================================================

#Question 5:
'''
Your monthly expense list (from Jan to May) looks like this,
expense_list = [2340, 2500, 2100, 3100, 2980]
Write a program that asks you to enter an expense amount and program should tell you in which month that
expense occurred. If expense is not found then it should print that as well.
'''
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January","February","March","April","May"]
expense_amount = int(input(f'Enter expense amount : '))
month = -1

for i in range(len(expense_list)):
    if(expense_amount == expense_list[i]):
        month = i
        break

if(month!=-1):
    print(f'You spent {expense_amount}$ in {month_list[month]}')
else:
    print(f'You did not spent {expense_amount}$ in any month')
    
    
#==============================================================
#Question 6: 
'''
Lets say you are running a 5 km race. 
Write a program that,
Upon completing each 1 km asks you "are you tired?"
If you reply "yes" then it should break and print "you didn't finish the race"
If you reply "no" then it should continue and ask "are you tired" on every km
If you finish all 5 km then it should print congratulations message
'''
print("Reply with Yes / No ")
for i in range(0,5):
    tired = str.lower((input(f'Are you tired after completing {i+1} km running : ')))
    if(i==4):
        print(f'Congratulation, You complete the 5km race' )
    elif(tired == 'yes'):
        print(f'You didn\'t finish the race')
        break
    elif(tired == 'no'):
        continue
    else:
        print(f'Invalid entry. only enter Yes / No')
        
#==============================================================
#Question 7:
''' Write a program that prints following shape
*
**
***
****
***** 
'''
# for i in range(1,6):
#     print('*' * i)
    
    #*OR using for nested loop outerloop for row shifting and inner loop adding star on current line

for i in range(0,6):
    s=''
    for j in range(i):
        s += '*'
    print(s)

                
    
































    


