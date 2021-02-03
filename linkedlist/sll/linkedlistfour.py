class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def findlengthofll(self):
        count = 0
        last = self.head
        while last:
            count+=1
            last = last.next
        return count
        
    def insertintoll(self,data):
        node  = Node(data)
        if self.head == None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next
        last.next = node


    def printlist(self):
        last = self.head
        while last:
            print(last.data,end="")
            last = last.next
        


l = LinkedList()
l.insertintoll(1)
l.insertintoll(2)
l.insertintoll(3)
l.insertintoll(4)
l.insertintoll(5)
l.insertintoll(6)
l.insertintoll(7)
l.insertintoll(8)
l.printlist()
length = l.findlengthofll()
print("\n",length)