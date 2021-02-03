class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0
    @property    
    def countnode(self):
        return self.count

    def insertintoll(self,data):
        self.count = self.count + 1        
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        last = self.head
        while last.next:
            last  = last.next

        last.next = newnode
        return
    def printll(self):
        last = self.head 
        while last:
            print(last.data , end=" ")
            last = last.next

    def remove(self,node):

        prev = None
        last = self.head 
        if self.count < node:
            print("Number of node in LL is less than your node")
            return

        while node-1:
            prev = last
            last = last.next
            node = node -1
        prev.next = last.next
        return            

l = LinkedList()
l.insertintoll(1)
l.insertintoll(2)
l.insertintoll(3)
l.insertintoll(4)
# l.printll()
l.remove(5)
l.printll()
print("\n Number of nodes in ll {}".format(l.countnode))