#Question 1
word_lst = ["python", "java", "c++"]

#word[start:stop:empty]
rev_word = [word[::-1] for word in word_lst]
print(rev_word)


#Question 2
#Generate a list of numbers between 1 and 50 that are divisible by both 3 and 5.
nums = [num for num in range(1,51) if num%3==0 and num%5==0]
print(nums)

#Question 3
# Given words = ["hi", "hello", "data", "AI", "python"],
# create a list of words longer than 3 characters and convert them to uppercase.
words = ["hi", "hello", "data", "AI", "python"]
new_words = [word.upper() for word in words if len(word)>3]
print(new_words)

#Question 4
# From words = ["madam", "racecar", "apple", "level", "banana"],
# create a new list of only palindromes.
words =  ["madam", "racecar", "apple", "level", "banana"]
palin_words = [word for word in words if word == word[::-1]]
print(palin_words)


# Question 5
# For A = [1, 2] and B = [3, 4]
# generate all possible pairs using list comprehension.

A = [1, 2]
B = [3, 4]
word_comb = [(a,b) for a in A for b in B]
print(word_comb)



