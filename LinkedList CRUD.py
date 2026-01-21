class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
        
class LinkedList():
    def __init__(self):
        self.head = None
        
    def empty(self):
        if not self.head:
            print("Linked list is empty")
            return
        
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def display(self):
        self.empty()
        current = self.head
        while current:
            print(current.data, end="->")
            current = current.next
    
    def delete(self,value):
        self.empty()
        current = self.head
        if current and current.data == value:
            self.head = current.next
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if current:
            prev.next = current.next
            
        
    def reverse(self):
        self.empty()
        current = self.head
        prev = None
        n = 0
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
            
        
ll = LinkedList()
for i in range(1,6):
    ll.append(i)
ll.display()
print("")
ll.delete(4)
ll.display()
print("")
ll.reverse()
ll.display()