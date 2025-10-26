#MarksManagement.py

from DataManager import Data

class MarksManager:
    def __init__(self, file_path=r'03_week_5_advanced_python/Python_Projects/05_Student_Performance_Analyzer/marks_records.json'):
        
        self.file_path = file_path
        self.data_obj = Data(self.file_path)
        self.std_data = self.data_obj.load_all_data()
        
    def add_student_result(self, teacher_username, std_name, roll_no, class_, **marks):
        roll_no = int(roll_no)
        for std in self.std_data:    #if student exist with roll no then stop
            if std['roll_no'] == roll_no:
                print("Result with this roll no already exist!")
                return
        
        total_marks = self.total_marks(**marks)
        percentage = self.calculate_percentage(**marks)
        grade_performance = self.assign_grade_and_tag(percentage)
        grade = grade_performance['grade']
        performance = grade_performance['performance']
        
        #if not then create new student
        new_record =   {
        "teacher_name": teacher_username,
        "name": std_name,
        "roll_no": roll_no,
        "class": class_,
        "marks": marks,
        "total": total_marks,
        "percentage": percentage,
        "grade": grade,
        "performance":performance
        }
        self.std_data.append(new_record)
        self.data_obj.save_all_data(self.std_data)

    def total_marks(self, **marks):
        total = 0
        for marks in marks.values():
            total += marks
        return total
    
    def calculate_percentage(self, **marks):
        total_obtained = sum(marks.values())
        possible_marks = 100 * len(marks)
        percentage = (total_obtained / possible_marks) * 100
        return round(percentage,2)
    
    def assign_grade_and_tag(self, percentage):
        """
        Assign grade and performance tag using match-case with guards."""
        grade_performance = {}

        match percentage:
            case p if 90 <= p <= 100:
                grade_performance['grade'] = 'A+'
                grade_performance['performance'] = 'Excellent'
            case p if 80 <= p < 90:
                grade_performance['grade'] = 'A'
                grade_performance['performance'] = 'Very Good'
            case p if 70 <= p < 80:
                grade_performance['grade'] = 'B'
                grade_performance['performance'] = 'Good'
            case p if 60 <= p < 70:
                grade_performance['grade'] = 'C'
                grade_performance['performance'] = 'Average'
            case p if 50 <= p < 60:
                grade_performance['grade'] = 'D'
                grade_performance['performance'] = 'Needs Improvement'
            case p if p < 50:
                grade_performance['grade'] = 'F'
                grade_performance['performance'] = 'Fail'
            case _:
                grade_performance['grade'] = 'N/A'
                grade_performance['performance'] = 'Invalid Percentage'

        return grade_performance

if __name__=='__main__':
    marks = {"Math": 85, "Science": 90, "English": 80}

    m1 = MarksManager()
    m1.add_student_result('nasreen', 'harry', 1, '10-A', **marks)


            
        
        
        
            
        
        
    