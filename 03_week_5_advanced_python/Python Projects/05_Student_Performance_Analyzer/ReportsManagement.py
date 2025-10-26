#ReportsManagement.py
from MarksManagement import MarksManager
from DataManager import Data
import matplotlib.pyplot as plt

class ReportsManager:
    def __init__(self, file_path=r'C:\Users\Admin\OneDrive\Desktop\Ai\03_week_5_advanced_python\Python Projects\05_Student_Performance_Analyzer\marks_records.json'):
        self.file_path = file_path
        self.data_obj = Data(self.file_path)
        self.std_data = self.data_obj.load_all_data()
        
    def view_all_students_result(self, teacher_username):
        teacher_found = False
        print(f"Result of Teacher {teacher_username} Students")
        # print(type(self.std_data))
        for result in self.std_data:
            if result['teacher_name'] == teacher_username:
                teacher_found = True
                print(f'{50 * '-'}')
                print(f'{50 * '-'}')
                print(f'Student Name : {result['name']}')
                print(f'Roll No : {result['roll_no']}')
                print(f'Class : {result['class']}')
                print(f'Marks : {result['marks']}')
                print(f'Total Marks : {result['total']}')
                print(f'Percentage : {result['percentage']}')
                print(f'Grade : {result['grade']}')
                print(f'Performance  : {result['performance']}')
        
        
        if not teacher_found:
            print(f"Teacher {teacher_username} has no student results.")          
            return
    
    def view_top_3_performer(self,teacher_username):
        teacher_std = []
        for result in self.std_data:
            if result['teacher_name'] == teacher_username:
                teacher_std.append(result)
        
        if not teacher_std:
            print(f"Teacher {teacher_username} has no student results to rank.")
            return
                
        sorted_std = sorted(teacher_std, key=lambda x:x['percentage'],  reverse=True)
        top_3 = sorted_std[0:3]
        for result in top_3:
                print(f'{50 * '-'}')
                print(f'{50 * '-'}')
                print(f'Teacher Name : {result['teacher_name'][:-2]}')
                print(f'Student Name : {result['name']}')
                print(f'Roll No : {result['roll_no']}')
                print(f'Class : {result['class']}')
                print(f'Marks : {result['marks']}')
                print(f'Total Marks : {result['total']}')
                print(f'Percentage : {result['percentage']}')
                print(f'Grade : {result['grade']}')
                print(f'Performance  : {result['performance']}')
            
    def view_subject_avg(self, teacher_username, class_name, subject):
        '''function for subject wise average marks'''
        records = []
        for res in self.std_data:
            if res['teacher_name'] == teacher_username and res['class'] == class_name:
                records.append(res)
        
        if not records:
            print(f"No record found with Teacher {teacher_username} and Class {class_name}")
            return
        
        subjects_marks = []
        for rec in records:
            for sub in rec['marks']:
                if sub == subject:
                    subjects_marks.append(rec['marks'][sub])
        
        avg = sum(subjects_marks)/len(records)                          
        return avg                    
        
    def avg_class_marks(self, teacher_username, class_name):
        records = []
        for res in self.std_data:
            if res['teacher_name'] == teacher_username and res['class'] == class_name:
                records.append(res)
                
        total_marks_class= 0
        for rec in records:
            total_marks_class += rec['total']
        avg = total_marks_class / len(records)
        return avg

    def filter_std(self,std_username, roll_no):
        '''print student with student name and roll no'''
        std_found = False
        for result in self.std_data:
            if result['name'] == std_username and result['roll_no'] == roll_no:
                std_found = True
                print(f'{50 * '-'}')
                print(f'{50 * '-'}')
                print(f'Student Name : {result['name']}')
                print(f'Roll No : {result['roll_no']}')
                print(f'Class : {result['class']}')
                print(f'Marks : {result['marks']}')
                print(f'Total Marks : {result['total']}')
                print(f'Percentage : {result['percentage']}')
                print(f'Grade : {result['grade']}')
                print(f'Performance  : {result['performance']}')
                return
        
        if std_found is False:
            print(f'Student Not found with username and password!')
            
    def visualize_avgMarks_allSub(self, teacher_username, class_name):
        found = False
        noOfStd = 0
        subjects_marks = {}
        for result in self.std_data:
            if result['teacher_name'] == teacher_username and  result['class'] == class_name:
                found = True
                noOfStd += 1
                for key,value in result['marks'].items():   #perform addition subject and append into dict
                        if key in subjects_marks:   
                            subjects_marks[key] += value 
                        else:
                            subjects_marks[key] = value
        
        #finding average marks for every subject in dict
        for key,value in subjects_marks.items():
            if key in subjects_marks:
                subjects_marks[key] = value/noOfStd
        
        if subjects_marks:
            plt.figure(figsize=(8,6))
            plt.bar(subjects_marks.keys(), subjects_marks.values(),  color=['blue', 'green', 'orange'])
            plt.title(f'Average Marks per Subject of Class {class_name}')
            plt.xlabel('Subjects')
            plt.ylabel('Average Marks')
            plt.grid(axis='y', linestyle='--', alpha=0.7) # Add a horizontal grid
            plt.show()
            return
        
        if found is False:
            print("No teacher and class available with these credentials!")
        
if __name__ == '__main__':
    r1 = ReportsManager()
    # r1.view_all_students_result('adil_a')
    # print(r1.view_top_3_performer('adil_a'))
    
    # print(r1.avg_class_marks('adil_a', '10-A'))
    
    # print(r1.view_subject_avg('adil_a', '10-A', 'Math'))
    
    r1.filter_std("John Dal", 106)
    
    # r1.visualize_avgMarks_allSub("adil", "10-A")


                
                
        
        
        