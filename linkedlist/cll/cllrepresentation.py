class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insertintocll(self,data):
        newnode = Node(data)
        print("newnode.data",newnode.data)
        if self.head == None:
            self.head = newnode
            newnode.next = self.head
            
            return
        last = self.head
        while last.next != self.head:
            last  = last.next
        last.next = newnode
        newnode.next = self.head
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
cll.insertintocll(5)
cll.printll()