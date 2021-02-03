class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueUsingLL(object):
    def __init__(self):
        self.head = None

    def enqueue(self,data):
        if self.head == None:
            self.head = Node(data)
            return
        newnode = Node(data)
        temp = self.head
        while temp.next is not None:

            temp = temp.next
        temp.next = newnode

    def dequeue(self):
        self.head = self.head.next
        return self.head

    def printqueueitems(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print("\n")                    

ll = QueueUsingLL()
ll.enqueue(1)
ll.enqueue(2)
ll.enqueue(3)
ll.enqueue(4)
ll.enqueue(5)
ll.enqueue(6)
ll.enqueue(7)
ll.enqueue(8)
ll.printqueueitems()
ll.dequeue()
ll.printqueueitems()