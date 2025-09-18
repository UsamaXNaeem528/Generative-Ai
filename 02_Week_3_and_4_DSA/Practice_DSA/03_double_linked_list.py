#============================================#
#       Double Linked List                   #
#============================================#

# -------------
# | P | D | N |
# -------------
class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.no = 0

    def __str__(self):
        curr = self.head
        result = ''
        while(curr != None):
            result = result + str(curr.data) + '->'
            curr = curr.next

        return result[:-2]
        
    def insert_head_node(self,data):
        if(self.head == None):    #if the list is empty
            new_node = Node(data)
            self.head = new_node
            self.no += 1
            return

        new_node = Node(data)      #if the list already contains a node
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
        self.no += 1
    
    def insert_tail_node(self,data):
        if(self.head  == None):
            return self.insert_head_node(data)
        
        curr = self.head
        while(curr!=None):
            if(curr.next==None):
                new_node = Node(data)
                curr.next = new_node
                new_node.prev = curr
                self.no += 1
                break
            curr = curr.next
            
    def insert_middle_node(self, after, value):
        curr = self.head
        while(curr!=None):
            if(curr.data == after):
                new_node = Node(value)
                new_node.next = curr.next
                curr.next = new_node
                new_node.prev = curr
                self.no += 1
                break
            curr = curr.next
        else:
            print("Item Not found")
    
    def delete_head_node(self):
        if(self.head == None):
            return print("List is empty")
        
        self.head = self.head.next
        self.no -= 1
    
    def delete_tail_node(self):
        if(self.head == None):
            return print("List is empty")
        
        curr = self.head
        if(curr.next == None):
            self.no -= 1
            return self.delete_head_node()

        while(curr!= None):
            if(curr.next.next == None):
                break
            curr = curr.next
            
        curr.next = None
        self.no -= 1
        
    def delete_node_by_value(self, value):
        curr = self.head

        # Step 1: Agar list empty hai
        if curr is None:
            print("List is empty!")  # kuch delete nahi ho sakta
            return

        # Step 2: Agar head node ko delete karna ho
        if curr.data == value:
            return self.delete_head_node()  # head ko direct delete karo

        # Step 3: Traverse the list for middle or tail node
        while curr is not None:

            # ✅ Safe check: Pehle ensure karo curr.next exists
            if curr.next and curr.next.data == value:

                # Special Case → Agar tail node delete ho rahi hai
                if curr.next.next is None:  
                    return self.delete_tail_node()  # tail node ko delete karo

                # Normal Case → Middle node delete
                curr.next = curr.next.next   # link ko bypass karo
                curr.next.prev = curr        # backward pointer update karo
                return  # delete ke baad exit

            curr = curr.next  # next node par move karo

        # Step 4: Agar pura loop traverse kar liya aur value nahi mili
        print("Node is not found")

    def del_node_by_index(self, index):
        curr = self.head
        pos = 0
        
        if(index == 0):
            return self.delete_head_node()
        
        while(curr!=None):
            if(pos == index-1):
                if(curr.next.next == None):
                    return self.delete_tail_node()
                    
                curr.next = curr.next.next   # link ko bypass karo
                curr.next.prev = curr  
                return
            curr =  curr.next
            pos += 1
    
    def search_by_value(self, value):
        pos = 0
        curr = self.head
        
        while(curr!=None):
            if(curr.data == value):
                return print(f'Node {curr.data} is found at index {pos}')
            curr = curr.next
            pos = pos + 1
        else:
            return print("Node is not found")
        
    def search_by_index(self, index):
        curr =  self.head
        pos = 0
       
        while(curr!=None):
            if(pos == index):
               return print(f"Node {curr.data} is present at index {pos}")
            pos += 1
            curr=curr.next
        else:
            print("Index outof range")
        
l1 = LinkedList()
l1.insert_head_node(10)
l1.insert_tail_node(20)
l1.insert_tail_node(30)
l1.insert_tail_node(40)
l1.insert_tail_node(50)
print(l1)
# l1.delete_node_by_value(30)
# l1.del_node_by_index(2)
# l1.search_by_value(50)
l1.search_by_index(9)
print(l1)