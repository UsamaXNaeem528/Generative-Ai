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
        self.data = value    # Node ka data
        self.next = None     # Node ka next pointer

# n1 = Node(10)
# n2 = Node(20)

# n1.next = n2
# print(f'{n1.data} | {n1.next}')
# print(f'{n2.data} | {n2.next}')


#=====================================
# 1. Pehle aik empty linked list create karte hain jisme initially koi nodes nahi hain.
# Agar head None hai to iska matlab list khali hai.
class LinkedList:
    def __init__(self):
        # head → list ka pehla node
        self.head = None
        # no. of nodes in linked list
        self.no = 0
        
    def __len__(self):
        return self.no
        
    def head_node(self, data):      # Start par node insert karna
        # naya node create karna
        new_node = Node(data)
        # naye node ka next purane head par point karega
        new_node.next = self.head
        # head ko naye node par set karna
        self.head = new_node
        self.no = self.no + 1
    
    def tail_node(self, data):  # List ke end par node add karna
        new_node = Node(data)
        # Agar list empty hai
        if self.head == None:
            self.head = new_node     
            return  
        else:
            curr = self.head
            # Last node tak traverse karna
            while(curr.next != None):    
                curr = curr.next
            # Last node ke next me naya node daal dena
            curr.next = new_node
        
        self.no += 1
            
    def __str__(self):            # Puri list ko string me print karna
        curr = self.head
        result = ''
        while(curr != None):
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]

    def insert_after(self, after, data):  # Kisi given node ke baad insert karna
        # Naya node banaya
        new_node = Node(data)
                
        # Traverse karne ke liye head ko curr me store kiya
        curr = self.head
        # List ko traverse karna jab tak hame "after" wala node na mil jaye
        while(curr != None):
            if(curr.data == after):
                break
            curr = curr.next
        
        # Agar node mil gaya
        if(curr != None):
            new_node.next = curr.next
            curr.next = new_node
            self.no += 1
        else:
            print("Item Not Found")  # Agar node nahi mila

    # Puri list ke sare nodes delete karna
    def delete_all_nodes(self):
        self.head = None
        self.no = 0
        
    # Head node delete karna
    def delete_head_node(self):
        self.head = self.head.next
        self.no -= 1
        
    # Tail node delete karna
    def delete_tail_node(self):
        curr = self.head
        
        # Agar list empty hai
        if(self.head == None):
            return print("List is empty, kuch delete nahi kar sakte!")
        
        # Agar list me sirf aik node hai
        if(curr.next == None):
            return self.delete_head_node()
        
        # Agar nodes aik se zyada hain
        while(curr.next.next != None):
            curr = curr.next
        
        # Second last node ke next ko None kar diya
        curr.next = None
        self.no -= 1
        
    # Node ko value ke basis par delete karna
    def delete_node_by_value(self, value):
        curr = self.head
        
        # 1. Agar list empty hai
        if(self.head == None):
            return print("List is empty")
        
        # 2. Agar jo node delete karna hai wo head node hai
        if(self.head.data == value):
            return self.delete_head_node()
        
        # 3. Traverse karna aur node dhoondhna
        while(curr.next != None):
            if(curr.next.data == value):
                break
            curr = curr.next
        
        # 4. Agar node nahi mili
        if(curr.next == None):
            return print("Item is not found!")
        else:    # Agar node mil gayi to pointer update karna
            curr.next = curr.next.next
            
        self.no -= 1
    
    def search_by_value(self, value):
        curr = self.head
        pos=0
        while(curr!=None):
            if(curr.data == value):
                return print("Node is found at index", pos)
            curr = curr.next
            pos = pos + 1
            
        return print("Node is not found")
    
    def __getitem__(self, index):
        curr = self.head
        pos=0
        while(curr!=None):
            if(pos == index):
                return print(f'Node index ==> {pos}\nData ==> {curr.data}')
            pos = pos + 1
            curr = curr.next
        
        return print("Node is not found")

    def delete_node_by_index(self, index):
        curr = self.head
        pos=0
        
        if(index == 0):
            return self.delete_head_node()
                
        while(curr.next!=None):
            if(pos == index-1):
                # curr.next = curr.next.next
                print("Node is found at pos",pos,"==>",curr.next.data)
                curr.next = curr.next.next
                return
            pos = pos + 1
            curr = curr.next

        
        



if __name__ == "__main__":
    # Testing linked list
    l1 = LinkedList()
    l1.head_node(10)
    l1.tail_node(12)
    l1.insert_after(10, 11)
    print(l1)
    # print(len(l1))

    # print("=====After deleting Nodes=====")
    # l1.delete_node_by_value(12)
    # # l1.delete_head_node()
    # print(l1)
    # print(len(l1))

    # l1.search_by_value(12)
    # l1[2]
    l1.delete_node_by_index(1)
    print(l1)