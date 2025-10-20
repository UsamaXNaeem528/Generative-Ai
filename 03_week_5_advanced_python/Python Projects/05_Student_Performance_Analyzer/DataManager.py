import json
class Data:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_all_data(self):          #read 
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data= json.load(f)
            return data
        except:
            return []
    
    def save_all_data(self, data):       #write
        '''Save all users into file'''
        with open(self.file_path, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
    
if __name__ == '__main__':
    d1 = Data(r'03_week_5_advanced_python\Python_Projects_IBHWSS\05_Student_Performance_Analyzer\users.json')
    print(d1.load_all_data())
    print(d1.file_path)
