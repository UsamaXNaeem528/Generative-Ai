import random
subject = {
    "politics": [
        "Imran Khan",
        "Nawaz Sharif",
        "Shehbaz Sharif",
        "Bilawal Bhutto Zardari",
        "Maryam Nawaz",
        "Asif Ali Zardari",
        "Pervez Elahi",
        "Shah Mehmood Qureshi",
        "Maulana Fazlur Rehman",
        "Hina Rabbani Khar"
    ],
    
    "celebrity": [
        "Mahira Khan",
        "Fawad Khan",
        "Sajal Aly",
        "Ahad Raza Mir",
        "Hania Aamir",
        "Iqra Aziz",
        "Yasir Hussain",
        "Ayeza Khan",
        "Mehwish Hayat",
        "Atif Aslam",
        "Ali Zafar",
        "Momina Mustehsan"
    ],
    
    "cricket": [
        "Babar Azam",
        "Shaheen Afridi",
        "Haris Rauf",
        "Shadab Khan",
        "Sarfraz Ahmed",
        "Mohammad Rizwan",
        "Shoaib Malik",
        "Shahid Afridi",
        "Wasim Akram",
        "Misbah-ul-Haq"
    ]
}

actions = {
    "politics": [
        "announced a new policy",
        "attended a secret meeting",
        "launched a campaign in the city",
        "criticized the opposition on social media",
        "visited flood-affected areas",
        "revealed plans for an international summit",
        "faced questions in parliament",
        "called for new elections",
        "met with foreign diplomats",
        "started a new charity initiative"
    ],
    
    "celebrity": [
        "launched a new movie project",
        "released a music album",
        "attended a fashion event",
        "posted a viral video on social media",
        "donated to charity",
        "announced a collaboration with a brand",
        "surprised fans with a live performance",
        "revealed personal news in an interview",
        "started a new acting workshop",
        "appeared on a talk show"
    ],
    
    "cricket": [
        "scored a century in the match",
        "joined a new cricket league",
        "announced retirement plans",
        "trained with the national team",
        "faced criticism for performance",
        "won the man of the match award",
        "participated in a charity cricket match",
        "shared training tips on social media",
        "attended a sports award ceremony",
        "announced cricket academy opening"
    ]
}

places = {
    "politics": [
        "at the National Assembly Building",
        "in Islamabad Secret Bunker",
        "at Lahore Press Club",
        "in Multan Mango Festival",
        "at Gwadar Space Center",
        "in Islamabad AI Conference",
        "at Faisal Mosque Rooftop",
        "in Peshawar Truck Art Museum",
        "at Karachi Digital Summit",
        "in Lahore Political Rally"
    ],
    
    "celebrity": [
        "at Karachi Film Studio",
        "in Lahore Virtual Reality Arena",
        "at Murree Snow Park",
        "in Karachi Underwater Restaurant",
        "at Lahore Fashion Street",
        "in Islamabad Celebrity Gala",
        "at Hunza Valley Resort",
        "in Dubai Mall",
        "at Lahore Music Festival",
        "in Karachi Tea Café"
    ],
    
    "cricket": [
        "at National Cricket Academy",
        "in Lahore Stadium",
        "at Karachi Cricket Club",
        "in Islamabad Sports Complex",
        "at Multan Cricket Ground",
        "in Skardu Floating Stadium",
        "at Peshawar Cricket Arena",
        "in Karachi Underwater Cricket Event",
        "at Lahore Indoor Cricket Arena",
        "in Gwadar Cricket Festival"
    ]
}

def save_news(news):
    file_path = r'03_week_5_advanced_python\Python_Projects_IBHWSS\fake_news.txt'
    with open(file_path, 'a', encoding='utf-8') as f:
        f.write(news+'.'+'\n')

def fake_news(user_choice):
    if(user_choice == 'politics'):
        Subject = random.choice(subject['politics'])
        Actions = random.choice(actions['politics'])
        Places = random.choice(places['politics'])
        news =  f'Fake News : {Subject +' '+ Actions +' '+Places}'
        save_news(news)
        print(news)
        return 
        
    elif(user_choice == 'celebrity'):
        Subject = random.choice(subject['celebrity'])
        Actions = random.choice(actions['celebrity'])
        Places = random.choice(places['celebrity'])
        news =  f'Fake News : {Subject +' '+ Actions +' '+Places}'
        save_news(news)
        print(news)
        return 
        
    elif(user_choice == 'cricket'):
        Subject = random.choice(subject['cricket'])
        Actions = random.choice(actions['cricket'])
        Places = random.choice(places['cricket'])
        news =  f'Fake News : {Subject +' '+ Actions +' '+Places}'
        save_news(news)
        print(news)
        return 

categories = ['cricket', 'celebrity', 'politics']

user_choice = input("What type of Fake News You want to generate Politics / Celebertiy / Cricket : ").strip().lower()
while(user_choice != 'no'):
    if user_choice not in categories:
        print("Enter Correct Choice")
        break
    fake_news(user_choice)
    choice_IsYes = input("Do you want to generate fake news again yes / no : ").strip().lower()
    if choice_IsYes == 'yes':
        pass
    else: 
        print("Thank You")
        break



    

    
    

