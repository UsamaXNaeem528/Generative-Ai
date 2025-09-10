"""Let us say your expense for every month are listed below,
January - 2200
February - 2350
March - 2600
April - 2130
May - 2190
Create a list to store these monthly expenses and using that find out,

1. In Feb, how many dollars you spent extra compare to January?
2. Find out your total expense in first quarter (first three months) of the year.
3. Find out if you spent exactly 2000 dollars in any month
4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this"""

expenses = [
    {"January": 2200},
    {"February" : 2350},
    {"March" : 2600},
    {"April" : 2130},
    {"May" : 2190}
]

#1. 
extra_exp_feb = expenses[1]['February'] - expenses[0]['January']
print(extra_exp_feb)

#2.
first_quarter_months = ["January", "February", "March"]
total = 0

for exp in expenses:
    for month, amount in exp.items():
        if month in first_quarter_months:
            total += amount

print(f'First Quarter Expenses : {total}')

#3.
for exp in expenses:
    for month, amount in exp.items():
        if amount == 2000:
            print(f'You spend {2000} in {month}')
else:
    print("You dont spend 2000 in any month")
    
#4.
expenses.append({"June": 1980})
print(expenses)

#5.
expenses[3]["April"] += 200 
print(expenses)

'''You have a list of your favourite marvel super heros.
heros=['spider man','thor','hulk','iron man','captain america']
Using this find out,

1. Length of the list
2. Add 'black panther' at the end of this list
3. You realize that you need to add 'black panther' after 'hulk',
   so remove it from the list first and then add it after 'hulk'
4. Now you don't like thor and hulk because they get angry easily :)
   So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool).
   Do that with one line of code.
5. Sort the heros list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
'''

heros=['spider man','thor','hulk','iron man','captain america']

#1.
print(len(heros))

#2.
heros.append("Black Panther")
print(heros)

#3.
heros.remove('Black Panther')
heros.insert(3, 'Black Panter')
print(heros)


#4.
heros[1:3] = ['doctor strange']
print(heros)

#5. 
heros.sort()
print(heros)

"""
Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function.
"""

num_list = []
max_num = int(input('Enter a max number : '))


for num in range(1,max_num):
    if num%2 != 0:
        num_list.append(num)
        
print("Odd Numbers : ", num_list)












