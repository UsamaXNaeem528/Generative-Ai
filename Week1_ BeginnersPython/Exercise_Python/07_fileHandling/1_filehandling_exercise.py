word_statistics = {}

with open(r'Week1_ BeginnersPython\Exercise_Python\07_fileHandling\poem.txt','r') as f:
    for line in f:
        words_list = line.split(' ')
        for word in words_list:
            if word in word_statistics:
                word_statistics[word.strip('\n')] += 1
            else:
                word_statistics[word.strip('\n')] = 1

#get the max number value of word
max_count = max(word_statistics.values())

#now print this value with word
for word, count in word_statistics.items():
    if count == max_count:
        print(f'"{word}" occurs {count} times')

'''
🔍 Logic Understanding
Aik loop chale ga word_statistics dictionary pe, jismein word aur count hoon gay.
Har iteration mein har key ki value (count) ko max_count ke saath compare karein gay.
Jahan pe value max_count ke barabar ho jayegi, us ka matlab hai ke wo word maximum time aaya hai.
Wo word maximum occurring word ho ga.
'''

text = 'Generative AI will change everything'
str_list = list(text)   # this will convert a string into single characters

vowel = ['a','e','i','o','u']
count = 0
for char in str_list:
    if char in vowel:
        count = count + 1
print(count)




  
        