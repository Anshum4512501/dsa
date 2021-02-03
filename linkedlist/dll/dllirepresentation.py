class Node:
    def __init__(self,data):
        self.pre = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertintodll(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return

        last = self.head 
        while last.next:

            last = last.next    
        newnode.pre = last
        last.next = newnode
    def printdll(self):
        last = self.head
        while last:
            print(last.data,end="->")
            last = last.next            
dll = DoublyLinkedList()
dll.insertintodll(1)
dll.insertintodll(2)
dll.insertintodll(3)
dll.insertintodll(4)

dll.printdll()