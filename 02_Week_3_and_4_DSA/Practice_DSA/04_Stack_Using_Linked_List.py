'''
Stack is data stuctre in programming based on rule of LIFO (last in first out)
'''
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        if(self.top == None):
            return True
        else:
            return False       
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
    
    def traversel(self):
        temp = self.top

        while(temp != None):
            print(temp.data)
            temp = temp.next
        
    def peek(self):
        if(self.is_empty()):
            print("Stack is empty")
        else:
            print("On Top Stack Value : ",self.top.data)
            
    def pop(self):
        if(self.is_empty()):
            print("Stack is empty")
        else:
            data = self.top.data
            self.top = self.top.next
            return data
    
    def size(self):
        temp = self.top
        size = 0
        
        if(self.is_empty()):
            print("Stack is Empty")
        else:
            while(temp!=None):
                size = size + 1
                temp =  temp.next
            # print(f'{size} items in stack')
            return size

#==============================#
# reverse a string using stack #
#==============================#
def reverse_str(text):
    s = Stack()
        
    for i in text:
        s.push(i)
        
    rev = ''
    while(not s.is_empty()):
        rev = rev + s.pop()
        
    print(rev)
    
# reverse_str('hello')

#============================#
# undo redo problem in stack #
#============================#
def text_editor(text, pattern):
    u = Stack()
    r = Stack()
    
    for i in text:
        u.push(i)
    
    for i in pattern:
        if i == 'u':
            data = u.pop()
            r.push(data)
        else:
            data = r.pop()
            u.push(data)
    
    result = ''
    while(not u.is_empty()):
        result = result + u.pop()
    print(result)

# text_editor('usama','uuu')

#==============================#
#stack bracket problem in stack#
#==============================#
def stack_bracket(expression):
    # make a stack
    s = Stack()       
    
    # we make a list pair brackets for matching the open with close brackets
    pairs = {
            ')':'(',
             '}':'{',
             ']':'[',
             '>':'<'
            }
    
    open_para = ['(', '[', '{', '<']
    close_para = [')',']','}','>']
    
    for i in expression:
        #if the bracket is open then push in stack
        if i in open_para:
            s.push(i)
        
        # if the bracket is closed then pop it 
        elif i in close_para:
            if s.is_empty():
                print("Stack is unbalaned -  Extra Closing bracket found")
                return

            top_value = s.pop()
            
            if top_value != pairs[i]:
                print(f'Stack is unbalanced unmatched opening and closing brackets, expected{pairs[i]} but got {top_value}')
                return
                
    #traversing for the remain brackets in a stack
    if not s.is_empty():
        print("Stack is unbalanced - some opening brackets not closed")
        
        result = ''
        while(not s.is_empty()):
            result = s.pop() + result 
        print("Remaining unmatched opening brackets:", result)
    else:
        print("Stack is balanced")            

# exp = "{[(a+b)(a-b)]}"       
# stack_bracket(exp)

#==============================#
#  Celebrity Problem in stack  #
#==============================#
# stack is only the Data strcuture solve the matrix problem in Order of n O(n)
L = [
    [0,0,1,1],
    [0,0,1,1],
    [0,0,1,0],
    [0,0,1,0]
]

def find_celeb(L):
    s = Stack()

    #populate elements in stack
    for i in range(len(L)):
        s.push(i)
    
    #find the celeb from matrix
    while s.size() >= 2:
        i = s.pop()
        j = s.pop()
        
        if L[i][j] == 0:
            # j is not a celebrity means (i) dont know the (j)
            s.push(i)
        else:
            # i is not celebrity
            s.push(j)
    
    celeb = s.pop()
    
    for i in range(len(L)):
        if i != celeb:
            if L[i][celeb] != 1 or L[celeb][i] != 0:
                print("No one celebrity")
                return
    print("The celebroty is", celeb)

find_celeb(L)


    


            
    



        
    
    
        
        


            
                    
# s = Stack()
# print("====Push in Stack====")
# str = "hello"
# s.reverse_str(str)
# s.traversel()






# print("====Pop from Stack====")
# s.pop()
# s.traversel()
# print("====Peek item in of Stack====")
# s.peek()
# print("====Size of Stack====")
# s.size()



