#Question1
'''
We have following information on countries and their population (population is in crores),

Country	Population
China	143
India	136
USA	    32
Pakistan	21

i. Using above create a dictionary of countries and its population
ii. Write a program that asks user for three type of inputs,
    a. print: if user enter print then it should print all countries with their population in this format,
    china==>143
    india==>136
    usa==>32
    pakistan==>21
    
    b. add: if user input add then it should fursther ask for a country name to add. If country already exist in our dataset then it should print that it exist and do nothing. If it doesn't then it asks for population and add that new country/population in our dictionary and print it
    c. remove: when user inputs remove it should ask for a country to remove. If country exist in our dictionary then remove it and print new dictionary using format shown above in (a). Else print that country doesn't exist!
    d. query: on this again ask user for which country he or she wants to query. When user inputs that country it will print population of that country.
'''

country_population = {
    'china' : '143',
    'india'  : '136',
    'usa' : '32',
    'pakistan' : '21'
}

def print_all():
    for key, value in country_population.items():
        print(f'{key} ==> {value}')
    return

def add():
    country_to_add  = str.lower((input(f'Enter country name you want to add : ')))
    if(country_to_add in country_population.keys()):
        print(f'{country_to_add} is already exist in data set.')
        return
    population = str.lower(input(f'Enter population of {country_to_add} : '))
    country_population.update({country_to_add : population})
    for key, value in country_population.items():
        print(f'{key} ==> {value}')

def remove():
    country_to_remove = str.lower(input('Enter country name you want to remove : '))
    if(country_to_remove in country_population.keys()):
        country_population.pop(country_to_remove)
        for key, value in country_population.items():
            print(f'{key} ==> {value}')
        return
    else:
        return print(f'{country_to_remove} is not exist in data set.')

def query():
    country_to_query = str.lower(input('Enter country name you want to query : '))
    if(country_to_query in country_population.keys()):
        print(f'{country_to_query} population is {country_population.get(country_to_query)}')
        return
    else:
        print(f'{country_to_query} is not exist in data set')
        return 

def main():
    print('Choose option print / add / remove / query')
    choice = input(f'Enter something from above options : ')
    
    if choice.lower() == 'print':
        print_all()
    elif choice.lower() == 'add':
        add()
    elif choice.lower() == 'remove':
        remove()
    elif choice.lower() == 'query':
        query()

if __name__ == '__main__':
    main()
    
    
        
    



    
    
    
 
    
    






