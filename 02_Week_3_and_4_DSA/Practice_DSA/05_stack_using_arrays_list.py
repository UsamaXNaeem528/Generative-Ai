#in this code stack is implemented using list or array using OOPs / classes
class Stack:
    def __init__(self,size):
        self.size = size  # Stack ki maximum capacity (kitne element aa sakte hain)
        self.stack = [None] * size     # Pehle se fixed size ka array allocate kar diya (jitna size otna list ka elements)
        self.top = -1                   # -1 ka matlab hai stack abhi khaali hai
    
    def push(self, data):
        #first we check is full or not (if it is full then we return the function & dont push more items)
        if self.size == self.top + 1:
            return print("Over flow")
        else:
            self.top += 1
            self.stack[self.top] =  data

    def pop(self):
        if self.top == -1:
            return print("Stack is empty")
        else:
            data = self.stack[self.top]
            self.top -= 1
            del data
    
    def traverse(self):
        
        for i in range(self.top + 1):
            print(self.stack[i], end=' ')
            
            
s = Stack(3)
s.push(1)
s.push(2)
s.push(3)
# s.push(4)
s.traverse()
print("\nPop the element")
s.pop()
s.traverse()
