
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedListReverse:
    def __init__(self):
        self.head  = None

    def insertintoll(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return

        last = self.head 
        while last.next:

            last  = last.next
        last.next = newnode        

    def printlist(self):
        last = self.head
        while last:
            print(last.data,end="")
            last  = last.next

    def reverselist(self):
        current = self.head
        prev = None
        while current is not None:

            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev    



l = LinkedListReverse()
l.insertintoll(1)
l.insertintoll(2)
l.insertintoll(3)
l.insertintoll(4)
l.reverselist()
l.printlist()