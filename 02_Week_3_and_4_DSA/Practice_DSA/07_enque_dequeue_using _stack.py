# Interview Question: Perform enqueue and dequeue using two stacks
class Stack:
    def __init__(self,size):
        self.size = size
        self.stack = [''] * size
        self.top = -1

    def push(self, data):
        self.top += 1
        self.stack[self.top] = data
    
    def pop(self):
        data =  self.stack[self.top]
        self.top -= 1
        return data
    
    def is_empty(self):
        return self.top == -1
            
    def traversel(self):
        for i in range(self.top+1):
            print(i, end=' ')   
    

            
        
            
class QueueUsingStack:
    def __init__(self, size):
        self.s1 = Stack(size)
        self.s2 = Stack(size)

    def enqueue(self,data):
        self.s1.push(data)
        print(f'Enqueued {data}')

    def dequeued(self):
        if(self.s2.is_empty() and self.s1.is_empty()):
            print("Stack is Empty")
            return
    
        #if the s2 is empty and s1 is not empty then using pop() move all item to and push in stack 2
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
                
        data =  self.s2.pop()
        print(f'Dequeued {data}')
        return data

    def Queue_Traversel(self):
        temp = []
        #take eleemnt from stack 2 in reverse order (N, -1)
        for i in range(self.s2.top,-1):
            temp.append(self.s2.stack[i])
        
        #take element from stack in asc order (1,N)
        for i in range(self.s1.top+1):
            temp.append(self.s1.stack[i])
        print(temp)
    
q1 = QueueUsingStack(5)
q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)
q1.enqueue(40)

q1.dequeued()
q1.Queue_Traversel()
q1.dequeued()
q1.Queue_Traversel()

q1.enqueue(50)
q1.enqueue(60)
q1.enqueue(70)
q1.enqueue(80)

q1.Queue_Traversel()


   
        
            
            

        
    




        
        
        
        
    
        
        
        

    
    
    
    
    