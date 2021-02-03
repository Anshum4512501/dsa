class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None


    def push(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        last = self.head    
        while last.next:
            last = last.next
        last.next = newnode





    def printlist(self):
        last = self.head    
        while last:
            print(last.data,end="")
            last = last.next



    def delete(self,nodenumber):
        pass
    



l = LinkedList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.printlist()