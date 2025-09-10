std_info = {

}

#module file
def std_to_dict(name, roll_no, email):
    std_info[roll_no] = {
        "name" : name,
        "email" : email
    }

def std_print():
    for roll_no, details in std_info.items():
        print(f'Student Roll No : {roll_no}')
        for key,value in details.items():
                print(f'{key} : {value}')
        

    
    






