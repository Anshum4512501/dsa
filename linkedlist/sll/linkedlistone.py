#representation of linked list
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            return 
            
        last = self.head
        while last.next:
            last = last.next

        last.next = newnode    

            


    def printlist(self):
        last = self.head
        while last:
            print(last.data,"->",end="")
            last = last.next
        



l = LinkedList()
l.insert(2)
l.insert(3)
l.insert(4)
l.insert(4)
l.insert(4)
l.insert(8)
l.insert(9)

l.printlist()
