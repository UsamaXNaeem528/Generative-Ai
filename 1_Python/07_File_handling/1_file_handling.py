
'''1. ✅Opening and Closing Files'''

'''Opening '''
#! file_object = open('filename.ext','mode')

'''Common Modes 
'r' - Read (default mode, opens for reading)
'w' - Write (creates new file or truncates existing one)
'a' - Append (opens for writing, appends to end if file exists)
'x' - Exclusive creation (fails if file exists)
'b' - Binary mode
't' - Text mode (default)
'+' - Updating (read and write)
'''

'''Closing Files Always close files when done to free resources'''
#! file_object.close()

'''Using Context Managers (Recommended)
The with statement automatically closes the file:'''
#! with open('file.txt', 'r') as file:
    # work with the file here
# file is automatically closed here

'''2. ✅Reading from File'''
# *Reading Entire Content
with open(r'Week1_ BeginnersPython\07_File_handling\file.txt','r') as file:
    content = file.read()
    print(content)

# *Reading Content line by line
with open(r'Week1_ BeginnersPython\07_File_handling\file.txt','r') as file:
    for line in file:
        print(line)
        
# *Reading All Lines into a List
list = []
with open(r'Week1_ BeginnersPython\07_File_handling\file.txt','r') as file:
    for line in file:
        list.append(line.strip('\n'))
    print(list)

# *Reading a Single Line
with open(r'Week1_ BeginnersPython\07_File_handling\file.txt','r') as file:
    line = file.readline()
    print(line)

'''3. ✅Writing to Files'''
#*Writing Strings
with open(r'Week1_ BeginnersPython\07_File_handling\write_file.txt','w') as file:
    file.write("Hello Usama is writng in to the file.")
    
#*Writing Multiple Lines
lines = ["My Name is Usama.\n", "Currently my interst in generative Ai.\n", "I am learning python for it.\n"]
with open(r'Week1_ BeginnersPython\07_File_handling\write_file.txt','w') as file:
    file.writelines(lines)
    
#* Appending to Files
with open(r'Week1_ BeginnersPython\07_File_handling\write_file.txt','a') as file:
    file.writelines('I am on file handling topic')
    


    

