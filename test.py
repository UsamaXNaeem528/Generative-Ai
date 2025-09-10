# # list_for_copy = ['Usama','Naeem','GenAi','LLM']
# # # copied_list = list_for_copy.copy()
# # #     # OR using list constructor
# # # # copied_list = list(list_for_copy)  

# # # copied_list.append("Computer Vision")
# # # print(copied_list) 
# # # print(list_for_copy)


# # std_list = {
# #     "name" : "Usama Naeem",
# #     "ph" : "03481499528"
# # }
# # # print(std_list.items())
# # std_list["name"] = "Hassan"

# # print(std_list)


# num_list = [1,2,3,4,5,6,7,8]

# even_num = list(map(lambda x: x**2, num_list))
# print(even_num)


# # nums = [1,3,5,7,9]
# # square = list(map(lambda x : x**2, nums)) #*maps the nums list to expression to find square. 
# # print(square)

# list = []
# with open(r'C:\Users\Admin\OneDrive\Desktop\Ai\1_Python\07_File_handling\file.txt','r') as file:
#     for line in file:
#         list.append(line.strip('\n'))
#     print(list)

# # Your monthly expense list (from Jan to May) looks like this,
# expense_list = [2340, 2500, 2100, 3100, 2980]
# # Write a program that asks you to enter an expense amount and program should tell you in which month that
# # expense occurred. If expense is not found in expense_list then it should print that as well.
# month_list = ["January","February","March","April","May"]

# exp_amount = int(input('dEnter expense amount you spend : '))

# found = False
# for exp, month in zip(expense_list,month_list):
#     if exp_amount == exp:
#         found = True
#         print(f'{exp_amount} spend in {month}')
#         break
# if not found:
#     print(f'No expenses found in month list')


# Lets say you are running a 5 km race. 
# Write a program that,
# Upon completing each 1 km asks you "are you tired?"
# If you reply "yes" then it should break and print "you didn't finish the race"
# If you reply "no" then it should continue and ask "are you tired" on every km
# If you finish all 5 km then it should print congratulations message

for i range(0,5):
    