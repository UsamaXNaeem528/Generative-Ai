# 🧩 What is an Iterator?

# An iterator is an object that allows you to traverse (go through)
# elements of a collection (like a list, tuple, or string) one at a time — without using indexing.
#one by one
# 🔹 How Iterator Works Internally
# To understand this, let’s use two built-in functions:
# iter() → creates an iterator object
# next() → returns the next element from the iterator

string = 'usama'
it = iter(string)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#so iter and next working to gether and iter creater iter object and next used to print the
#elements from next.



# make an iterator that print the number from 1 to n
class Count:
    def __init__(self, limit):      #limit define the range from 1 to number stop
        self.limit = limit
        self.num = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num <= self.limit:
            value  = self.num
            self.num += 1
            return value
        else:
            raise StopIteration
    
for i in Count(10):
    print(i)


#count down iterator
class CountDown:
    def __init__(self,num):
        self.num = num
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.num > 0:
            value = self.num
            self.num -= 1
            # if(self.num == -1):
            #     return
            return value
        else:
            raise StopIteration

for i in CountDown(10):
    print(i)


#Create an iterator that takes a string and returns one character at a time.
class stringIterator:
    def __init__(self,str_1):
        self.str_1 = str_1
        self.limit = len(str_1)
        self.index = 0
        
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.limit > self.index:
            ch = self.str_1[self.index]
            self.index += 1
            return ch
        else:
            raise StopIteration

for ch in stringIterator("Usama"):
    print(ch)



# | Feature               | Iterable                | Iterator                        |
# | --------------------- | ----------------------- | ------------------------------- |
# | Kya karta hai         | Data ko store karta hai | Data ko ek-ek karke nikalta hai |
# | Method                | `__iter__()`            | `__iter__()` + `__next__()`     |
# | Example               | list, tuple, string     | iter(list), iter(tuple)         |
# | Create kaise hota hai | Python se default       | `iter()` function se            |
# | Use kab hota hai      | jab loop lagate ho      | jab next() call karte ho        |
# | Kaun pehle            | Iterable                | Iterator (baad mein)            |

# Iterable wo hota hai jisko loop kiya ja sakta hai.
# Iterator wo hota hai jo loop ke andar har step pe value deta hai.

    
    
