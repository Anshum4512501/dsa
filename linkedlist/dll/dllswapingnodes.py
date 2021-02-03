class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None

class DLL:
    def __init__(self):
        self.head = None

    def insertintodll(self,data):
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        
        newnode.next = self.head
        self.head = newnode

    def swapping(self,data_one,data_two):
        last = self.head

        while last.data != data_one:
            last = last.next
    
        node_one = last
        last = self.head
        while last.data != data_two:
            last = last.next
        node_two = last
# to do (still replacements of nodes have to be done)
        node_one.prev.next = node_two
        node_two.prev.next = node_one        
            
    def printdll(self):
        last = self.head 
        print("\n")
        while last:
            print(last.data,end=" ")
            last = last.next                    

dll = DLL()
dll.insertintodll(1)
dll.insertintodll(2)
dll.insertintodll(3)
dll.insertintodll(4)
dll.insertintodll(5)
dll.insertintodll(6)
dll.printdll()
dll.swapping(2,5)
dll.printdll()

