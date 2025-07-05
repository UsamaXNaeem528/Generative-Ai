# # '''7. ✅Working with CSV Files'''
# # '''Reading CSV Files'''
# import csv
# with open(r'Week1_ BeginnersPython\07_File_handling\data.csv','r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)
        
# '''Writing to CSV Files'''
# data = [['Name', 'Age'], ['Alice', 25], ['Bob', 30]]
# with open(r'Week1_ BeginnersPython\07_File_handling\data.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(data)
    
# ''' 7.✅Working with CSV Files'''
import json
# '''Reading a json'''
# with open(r'Week1_ BeginnersPython\07_File_handling\data.json','r') as file:
#     read_json = json.load(file)
    
# print(read_json["students"])

# '''Wrting to a json'''
# data = {
#     'students' : [
#         {"name": "Alice", "age": 21, "grade": "A"},
#         {"name": "Bob", "age": 20, "grade": "B"}
#     ]
# }
# with open(r'Week1_ BeginnersPython\07_File_handling\data.json','w') as file:
#     writer = json.dump(data, file, indent=4)
    
'''appending to the json'''
#step1 : read json 
with open(r'Week1_ BeginnersPython\07_File_handling\data.json','r') as file:
    data = json.load(file)
    
#step2 : moodify 
    data['students'].append({"name" : "Usama", "age" : 23, "grade" : "F+"})

#step 3 : write back
with open(r'Week1_ BeginnersPython\07_File_handling\data.json','w') as file:
    json.dump(data, file, indent=4)

    
    
    

    
    