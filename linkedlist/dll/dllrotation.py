class Node:
    def __init__(self,data):
        self.next = None
        self.data = data
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None

    def insertintodll(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return

        last = self.head
        while last.next :
            last  = last.next
        last.next = newnode
        newnode.prev = last    
        

    def printdll(self):
        last = self.head
        
        while last:
            print(last.data,end=" ")
            last = last.next



    def rotatedllbynode(self,n):
        
        last = self.head
        
        for _ in range(0,n):
            last = last.next

        temphead = last

        while last.next:
            last = last.next

        last.next = self.head
        self.head.prev = None
        temphead.prev.next = None
        self.head = temphead
        self.head.prev = None    
        print("\n")
            

        

dll = DLL()
dll.insertintodll(1)
dll.insertintodll(2)
dll.insertintodll(3)
dll.insertintodll(4)
dll.printdll()
dll.rotatedllbynode(1)
dll.printdll()