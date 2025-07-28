#multiple inheritence -> one derived / child class can inherit the two base / parent classes

class Student:
    def __init__(self, name, std_id):
        self.name = name
        self.std_id = std_id
        
    def display_student_info(self):
        print(f'Student Name : {self.name}\nStudent ID : {self.std_id}')
    
class Athlete:
    def __init__(self, sport):
        self.sport = sport
    
    def display_athlete_info(self):
        print(f'Sports name : {self.sport}')
        
class StudentAthlete(Student, Athlete):
    def __init__(self, name, std_id, sport):
        Student.__init__(self, name, std_id)
        Athlete.__init__(self, sport)
        
    def dispaly_full_info(self):
        self.display_student_info()
        self.display_athlete_info()
        
st1 = StudentAthlete('Usama', 'ST23', 'Cricket')
st1.dispaly_full_info()


#by using super().__init__(self, name, age)  --> we can access the parent classes properties in derived

        