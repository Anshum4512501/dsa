class Node:
    def __init__(self,data):
        self.pre  = None
        self.data = data
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    def insertatbeg(self,data):
        newnode = Node(data)
        if self.head == None:

            self.head = newnode
            return 
        newnode.next     = self.head
        newnode.next.pre = newnode
        self.head        = newnode


    def printdll(self):
        last = self.head 
        while last:
            print(last.data,end=" ")
            last = last.next

dll = DLL()
dll.insertatbeg(1)
dll.insertatbeg(2)
dll.insertatbeg(3)
dll.insertatbeg(4)
dll.insertatbeg(5)
dll.printdll()