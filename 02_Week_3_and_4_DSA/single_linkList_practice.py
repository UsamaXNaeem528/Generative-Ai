class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.no = 0
    
    def __len__(self):
        return self.no
    
    #==========================================#
    #         Traversing                       #
    #==========================================#
    def __str__(self):
        curr = self.head
        result = ''
        while(curr != None):
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]
        
    #==========================================#
    #           Node Insertion                 #
    #==========================================#
    
    def insert_head_node(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.no += 1
    
    def insert_tail_node(self, data):
        curr = self.head
        new_node = Node(data)
        
        if(self.head == None):
            return self.insert_head_node(data)
            
        while(curr!=None):
            if(curr.next == None):
                curr.next = new_node
                break
            curr=curr.next
        self.no += 1
        
    def insert_node_at_middle(self, after, data):
        curr = self.head
        new_node = Node(data)
        
        while(curr!=None):
            if(curr.data == after):
                break
            curr = curr.next
            
        if(curr!=None):
            new_node.next = curr.next
            curr.next = new_node
            self.no += 1
        else:
            print("Node is not found")

    #==========================================#
    #           Node Deletion                  #
    #==========================================#
    
    def del_head_node(self):
        if(self.head == None):
            return print("List is empty No head node found!")
        self.head = self.head.next
        self.no -= 1

    def del_tail_node(self):
        curr = self.head
        
        if(self.head == None):       #list is empty
            return print("List is empty No node found!")
        
        if(curr.next == None):      #single node in list
            return self.del_head_node
        
        while(curr!=None):           #traverse to the last node
            if(curr.next.next == None):
                curr.next = None
            curr = curr.next
        
        self.no -= 1
    
    def del_node_by_value(self, value):
        if(self.head == 0):
            return print("List is empty no node to delete")
        
        if(self.head.data == value):
            return self.del_head_node()
               
        curr = self.head
        
        while(curr!=None):
            if(curr.next.data == value):
                curr.next = curr.next.next
                self.no -= 1
                break
            curr = curr.next
    
    def del_node_by_index(self, index):
        curr = self.head
        pos = 0
        
        if(self.head == None):
            return print("List is empty no node to delete")
        
        if(index == 0):
            return self.del_head_node()

        while(curr.next!=None):
            if(pos == index - 1):
                curr.next = curr.next.next
                self.no -= 1
                return
            pos = pos + 1
            curr = curr.next 

    #==========================================#
    #           Node Searching                 #
    #==========================================#
    
    def search_node_by_value(self, value):
        if(self.head == None):
            return print("List is empty no node found")
        
        curr = self.head
        pos = 0
        while(curr!=None):
            if(curr.data == value):
                return print(f'Node {curr.data} is found at index {pos}')
            pos = pos + 1
            curr = curr.next
    
    def search_node_by_index(self, index):
        if(self.head == None):
            return print("List is empty no node found")
        
        curr = self.head
        pos = 0
        while(curr!=None):
            if(pos == index):
                return print(f"Node {curr.data} is present at index {pos}")
            pos = pos + 1
            curr = curr.next
        
        if(curr == None):
            return print("Index out of range")
            
if __name__ == "__main__":                              
    l1 = LinkedList()
    l1.insert_head_node(10)
    l1.insert_head_node(20)
    l1.insert_tail_node(30)
    # l1.insert_node_at_middle(10,20)
    l1.del_node_by_index(2)
    print(l1)