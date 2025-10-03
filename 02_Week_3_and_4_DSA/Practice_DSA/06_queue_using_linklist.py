#Linked list is the data structure based on FIFO principle First in first out.
#example like people stand in queue for buying the ticket so, 1st person in queue exit first and so on.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.front = None
        self.rear = None
    
    def enqueue(self,data):
        new_node = Node(data)
        #first check queue is empty (if empty then put node as front and rear both)
        if self.rear == None:
           self.rear = new_node
           self.front = self.rear
        else:  #if queue already contains nodes
            self.rear.next =  new_node
            self.rear = new_node
    
    def dequeue(self):
        if self.rear == None:
            print("Queue is empty")
            return 
        else:
            self.front = self.front.next        
    
    def traverse(self):
        temp = self.front
        while(temp!=None):
            print(temp.data, end=' ')
            temp = temp.next
    
    def is_empty(self):
        if self.rear == None:
            # print("Queue is empty")
            return True
        else:
            return False
    
    def get_rear(self):
        if self.is_empty():
            return
        else:
            return print(self.rear.data)

    def get_front(self):
        if self.is_empty():
            return
        else:
            return print(self.front.data)
    
    def size(self):
        temp = self.front
        count = 0
        
        while(temp!=None):
            count += 1
            temp = temp.next
            
        print(count)    

q = LinkedList()
# q.enqueue(1)
# q.enqueue(2)
# q.enqueue(3)
# q.traverse()
# print("\n")
# q.size()
# q.get_front()
# q.get_rear()
# print("\n")

# print(q.is_empty())
                

        