########################################################################################
############################* STRINGS IN PYTHON *#######################################
########################################################################################

##! 🔹 1. What is a String?
# A string is a sequence of characters, enclosed in quotes.
name = "Usama"
Age = "23"
print(f'My name is {name} and Age is {Age}')
##! You can use single (') or double (") quotes.


##! 🔹 2. Multi-line Strings
bio = '''I am learning a Python For become a Generative Ai Engineer.
I am a student of Computer Science.'''
print(bio)


##!🔹 3. String Operations
# ✅ Concatenation (joining strings)
background = "Computer Science"
profession_interset = "Generative AI Engineer"
print(f"My name is {name} and Age is {Age}. I am student of {background} and intersted to become a {profession_interset}")

# ✅ Repetition
print("Usama" * 3) # Repeats the string 3 times like UsamaUsamaUsama

# ✅ Length of a string
text = "UsamaNaeem"
print(len(text))


##! 🔹 4. String Indexing and Slicing
myString = "Hello,World!"
#* ✅ Indexing
print(myString[0])
print(myString[-1])
print(myString[-12])

#* ✅ Slicing (means print a some letters of string by giving range [0:3])
print(myString[0:5]) #* Pyt (start at 0, end before 5)
print(myString[6:]) #* print from sixth index to so on.
print(myString[:2]) #* print all indexes before fifth index.


##! 🔹 5. String Methods (Built-in Functions)
'''
| Method           | What it does                     |
| ---------------- | -------------------------------- |
| `.lower()`       | Converts to lowercase            |
| `.upper()`       | Converts to uppercase            |
| `.capitalize()`  | Capitalizes the first letter     |
| `.strip()`       | Removes whitespace               |
| `.replace(a, b)` | Replaces "a" with "b"            |
| `.find(word)`    | Finds the index of a word        |
| `.split()`       | Splits string into list of words |
'''
str_lower= 'Hello World'
print(str_lower.lower())

str_lower = str_lower.replace('Hello','Ai')
print(str_lower)

print(str_lower.split(" "))  #* word is break from space and convert into list

##! 🔹 6. f-Strings (String Formatting)
name = "Usama"
age = 23
print(f"My name is {name} and I'm {age} years old.")


##! 🔹 7. String Checks
word = "Python"

print(word.isalpha())     # True (only letters)
print(word.isdigit())     # False
print(word.islower())     # False
print(word.startswith("Py"))  # True
print(word.endswith("on"))    # True

##! 🔹 8. Escape characters
# An escape character is used to insert special characters into a string that are otherwise hard
# or impossible to type directly.
# In Python, the escape character is a backslash (\).

'''
| Escape | Meaning                      | Example                    | Output               |
| ------ | ---------------------------- | -------------------------- | -------------------- |
| `\n`   | New line                     | `"Hello\nWorld"`           | Hello                |
|        |                              |                            | World                |     
| `\t`   | Tab (horizontal space)       | `"Hello\tWorld"`           | Hello    World       |
| `\"`   | Double quote inside a string | `"She said, \"Hi!\""`      | She said, "Hi!"      |
| `\'`   | Single quote inside a string | `'It\'s nice'`             | It's nice            |
| `\\`   | Backslash itself             | `"Path: C:\\Users\\Usama"` | Path: C:\Users\Usama |
'''

qoute = "Learn not just to code, but to think.\nErrors teach more than success can bring.\nPatience and practice shape the way,\nOne small step, every single day."
print(qoute)

appreciation = "Usama is a \"Good Gen Ai Engineer!\""
print(appreciation)







