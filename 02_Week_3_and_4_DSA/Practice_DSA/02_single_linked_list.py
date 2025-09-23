"""
Array me kuch major problems the: (jo linked list solve karti hai)

1. Fixed size → resize costly hota hai.
2. Insertion/Deletion slow hota hai kyun ke shifting karni padti hai.
3. Continuous memory chahiye hoti hai, jo kabhi-kabhi available nahi hoti.
4. Dynamic arrays me copying overhead hota hai.

Linked List ke advantages:
1. Dynamic size hota hai.
2. Insertion/Deletion easy hota hai (shifting nahi karni parti).
3. Scattered memory ka use karti hai pointers ke saath.

Simple rule:
- Agar fast random access chahiye → Array use karo.
- Agar frequent insert/delete operations chahiye → Linked List use karo.
"""

#! Array values ko continuous memory location par store karta hai,
#! jab ke linked list nodes ko scattered memory me store karti hai
#! aur unhe pointers ke zariye connect karti hai.

# Manual tareeqe se aik individual node banate hain aur connect karte hain
# |data|next|
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
    
    def find_max_and_replace(self, value):
        curr = self.head
        max = curr
        while(curr!=None):
            if(curr.data>max.data):
                max = curr
            curr = curr.next
        max.data = value
    
    def sum_odd_nodes_value(self):
        curr = self.head
        index = 1
        result = 0

        while(curr!=None):
            
            if(index % 2 != 0):
                result = result + curr.data
                
            index = index + 1
            curr = curr.next
            
        return print(result)
    
    def print_reverse_order(self):
        prev_node = None
        curr_node = self.head
        while(curr_node!=None):
            next_node = curr_node.next    #2 nodes ma connection break karne ka liye curr node ka next ka adddres kisi variable store kare ga taake traver karsake linked list ma
            curr_node.next = prev_node    #curr node ka next ma None a gya 
            prev_node = curr_node         
            curr_node = next_node
        self.head = curr_node

"""
Array me kuch major problems the: (jo linked list solve karti hai)

1. Fixed size → resize costly hota hai.
2. Insertion/Deletion slow hota hai kyun ke shifting karni padti hai.
3. Continuous memory chahiye hoti hai, jo kabhi-kabhi available nahi hoti.
4. Dynamic arrays me copying overhead hota hai.

Linked List ke advantages:
1. Dynamic size hota hai.
2. Insertion/Deletion easy hota hai (shifting nahi karni parti).
3. Scattered memory ka use karti hai pointers ke saath.

Simple rule:
- Agar fast random access chahiye → Array use karo.
- Agar frequent insert/delete operations chahiye → Linked List use karo.
"""

#! Array values ko continuous memory location par store karta hai,
#! jab ke linked list nodes ko scattered memory me store karti hai
#! aur unhe pointers ke zariye connect karti hai.

# Manual tareeqe se aik individual node banate hain aur connect karte hain
# |data|next|
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
            result = result + str(curr.data) 
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
    
    def find_max_and_replace(self, value):
        curr = self.head
        max = curr
        while(curr!=None):
            if(curr.data>max.data):
                max = curr
            curr = curr.next
        max.data = value
    
    def sum_odd_nodes_value(self):
        curr = self.head
        index = 1
        result = 0

        while(curr!=None):
            
            if(index % 2 != 0):
                result = result + curr.data
                
            index = index + 1
            curr = curr.next
            
        return print(result)
    
    def print_reverse_order(self):
        prev_node = None
        curr_node = self.head
        while(curr_node!=None):
            next_node = curr_node.next    #2 nodes ma connection break karne ka liye curr node ka next ka adddres kisi variable store kare ga taake traver karsake linked list ma
            curr_node.next = prev_node    #curr node ka next ma None a gya 
            prev_node = curr_node         
            curr_node = next_node 
        self.head = prev_node
    
    def str_pattern_list(self):
        curr = self.head
        result = ''
        while(curr!=None):
            if(curr.data == '/' or curr.data == '*'):
                curr.data = ' '
                if(curr.next.data == '*' or curr.next.data == '/'):
                    curr.next.next.data = curr.next.next.data.upper()
                    curr.next = curr.next.next
            result = result + curr.data
            curr = curr.next
        return result
            
if __name__ == "__main__":                              
    l1 = LinkedList()
    input_str = "A,n,*,/,a,p,p,l,e,*,a,/,d,a,y,*,*,k,e,e,p,s,/,a,/,d,o,c,t,o,r,*,A,w,a,y"
    
    for char in input_str.split(','):
        node = char
        l1.insert_tail_node(node)

    print("Original Linked List:")
    print(l1)
    
    print("Link List after remove character:")    
    print(l1.str_pattern_list())
    # print(l1)


