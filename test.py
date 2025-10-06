# '''
# Stack is data stuctre in programming based on rule of LIFO (last in first out)
# '''
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
    
# class Stack:
#     def __init__(self):
#         self.top = None
    
#     def is_empty(self):
#         if(self.top == None):
#             return True
#         else:
#             return False       
    
#     def push(self, data):
#         new_node = Node(data)
#         new_node.next = self.top
#         self.top = new_node
    
#     def traversel(self):
#         temp = self.top

#         while(temp != None):
#             print(temp.data)
#             temp = temp.next
        
#     def peek(self):
#         if(self.is_empty()):
#             print("Stack is empty")
#         else:
#             print("On Top Stack Value : ",self.top.data)
            
#     def pop(self):
#         if(self.is_empty()):
#             print("Stack is empty")
#         else:
#             data = self.top.data
#             self.top = self.top.next
#             return data
    
#     def size(self):
#         temp = self.top
#         size = 0
        
#         if(self.is_empty()):
#             print("Stack is Empty")
#         else:
#             while(temp!=None):
#                 size = size + 1
#                 temp =  temp.next
#             print(f'{size} items in stack')
            
# def reverse_str(text):
#     s = Stack()
        
#     for i in text:
#         s.push(i)
        
#     rev = ''
#     while(not s.is_empty()):
#         rev = rev + s.pop()
        
#     print(rev)
    
# # reverse_str('hello')

# #undo redo problem in stack
# def text_editor(text, pattern):
#     u = Stack()
#     r = Stack()
    
#     for i in text:
#         u.push(i)
    
#     for i in pattern:
#         if i == 'u':
#             data = u.pop()
#             r.push(data)
#         else:
#             data = r.pop()
#             u.push(data)
    
#     result = ''
#     while(not u.is_empty()):
#         result = result + u.pop()
#     print(result)

# # text_editor('usama','uuu')

# #stack bracket problem in stack
# def stack_bracket(expression):
#     s = Stack()
    
#     # Mapping closing to opening brackets
#     pairs = {')': '(', '}': '{', ']': '[', '>': '<'}
#     open_para = ['(', '{', '[', '<']
#     close_para = [')', '}', ']', '>']
    
#     for i in expression:
#         # Push opening bracket
#         if i in open_para:
#             s.push(i)
        
#         # Closing bracket handling
#         elif i in close_para:
#             # If stack empty → extra closing bracket
#             if s.is_empty():
#                 print("Stack is unbalanced - extra closing bracket found")
#                 return
            
#             # Pop the top opening bracket
#             top_value = s.pop()
            
#             # Check if it matches the expected opening
#             #[{(]
#             if pairs[i] != top_value:
#                 print(f"Stack is unbalanced - mismatch found: expected {pairs[i]}, got {top_value}")
#                 return
    
#     # After traversing the expression
#     if not s.is_empty():
#         print("Stack is unbalanced - some opening brackets not closed")
#         result = ''
#         while not s.is_empty():
#             result = s.pop() + result
#         print("Remaining unmatched opening brackets:", result)
#     else:
#         print("Stack is balanced ✅")


# exp = "{[("       
# stack_bracket(exp)
        
    
    
        
        


            
                    
# # s = Stack()
# # print("====Push in Stack====")
# # str = "hello"
# # s.reverse_str(str)
# # s.traversel()






# # print("====Pop from Stack====")
# # s.pop()
# # s.traversel()
# # print("====Peek item in of Stack====")
# # s.peek()
# # print("====Size of Stack====")
# # s.size()




print(int(2.6457513))