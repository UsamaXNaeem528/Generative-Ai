# 👨‍💻 3. Quiz App (MCQs) – CLI
# Skills Learned: file I/O, lists/dictionaries, conditions, score system
# Load questions from JSON or text
# Ask one by one with options (A/B/C/D)
# Track score
# Show final result
# ➡️ Great for strengthening logic and loops.

questions = []
marks = []
score_save = []
import json

#load questions
file_path = r'3_Quiz_Cli_App/question.json'
with open(file_path, 'r', encoding='utf-8') as json_file:
   questions =  json.load(json_file)
   
#load previous scores
try:
    with open(r'3_Quiz_Cli_App\save_score.json', 'r', encoding='utf-8') as json_file:
        score_save =  json.load(json_file)
except (json.decoder.JSONDecodeError, FileNotFoundError):
        "No Score is saved"

def ask_question():
    print("\nEach Question Contains 5 marks")
    i = 1
    for i,question in enumerate(questions,start=1):
        print(f'{i}. {question['question']}')
        print(f'-Options')
        for key,value in question['options'].items():
            print(f'{key} : {value}')

        ans = input("Choose the correct Option (A/B/C/D): ").upper()
        if(ans == question['answer']):
            marks.append(5)
        else:
            marks.append(0)
        print('-' * 20)
    
def track_and_save_score(name):
    score = sum(marks)
    total_marks = len(questions) * 5
    print(f'\n🎯 You score a {score} marks out of {total_marks}')
    
    score_entry = {"name" : name, "score": score}
    score_save.append(score_entry)
    
    with open(r'3_Quiz_Cli_App\save_score.json','w',encoding='utf-8') as json_file:
        json.dump(score_save,json_file, indent=4)

def show_high_score():
    sorted_score = sorted(score_save, key=lambda x: x['score'], reverse=True)
    print(sorted_score)
# show_high_score()

#Main App
print("Welcome to the Quiz App.")
print("Enter 'Yes' for Play a Quiz")
print("Enter 'No' to exit\n")
while True:
    choice = str(input("Enter Your choice : ")).lower()    
    if(choice == 'yes'):
        name = str(input("Enter your name : "))
        marks.clear() #--> for clearing previous quiz marks
        ask_question()
        track_and_save_score(name)
    elif(choice.lower == 'no'):
        print("Thank you for playing the Quiz App. 👋")
        break
    else:
        print("❌ Invalid input. Please enter 'Yes' or 'No'")
        
