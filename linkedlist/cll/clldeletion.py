class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

# ToDo (Still error while deleting first node)
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertintocll(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            newnode.next = self.head
            return
        last = self.head 
        while last.next is not self.head:
            last = last.next

        last.next = newnode
        newnode.next = self.head
        return        

    def deletefromcll(self,node):
        last = self.head
        prev = None
        while node-1 :
            prev = last
            last = last.next
            node = node - 1
        if last.next == self.head:
            prev.next = self.head
            return
        prev.next = last.next
        return





    def printll(self):
        last = self.head
        
        while True:
            print(last.data,end=" ")
            if last.next is self.head:
                break
            
            last  = last.next
    


cll = CircularLinkedList()
cll.insertintocll(1)
cll.insertintocll(2)
cll.insertintocll(3)
cll.insertintocll(4)
cll.deletefromcll(1)
cll.printll()