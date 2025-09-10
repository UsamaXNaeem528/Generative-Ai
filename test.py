# list_for_copy = ['Usama','Naeem','GenAi','LLM']
# # copied_list = list_for_copy.copy()
# #     # OR using list constructor
# # # copied_list = list(list_for_copy)  

# # copied_list.append("Computer Vision")
# # print(copied_list) 
# # print(list_for_copy)


# std_list = {
#     "name" : "Usama Naeem",
#     "ph" : "03481499528"
# }
# # print(std_list.items())
# std_list["name"] = "Hassan"

# print(std_list)


num_list = [1,2,3,4,5,6,7,8]

even_num = list(map(lambda x: x**2, num_list))
print(even_num)


# nums = [1,3,5,7,9]
# square = list(map(lambda x : x**2, nums)) #*maps the nums list to expression to find square. 
# print(square)

list = []
with open(r'C:\Users\Admin\OneDrive\Desktop\Ai\1_Python\07_File_handling\file.txt','r') as file:
    for line in file:
        list.append(line.strip('\n'))
    print(list)