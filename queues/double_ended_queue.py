# Deque()         creates a new deque that is empty. It needs no parameters and returns an empty deque.
# add_front(item) adds a new item to the front of the deque. It needs the item and returns nothing.
# add_rear(item)  adds a new item to the rear of the deque. It needs the item and returns nothing.
# remove_front()  removes the front item from the deque. It needs no parameters and returns the item. The deque is modified.
# remove_rear()   removes the rear item from the deque. It needs no parameters and returns the item. The deque is modified.
# is_empty()      tests to see whether the deque is empty. It needs no parameters and returns a boolean value.
# size()          returns the number of items in the deque. It needs no parameters and returns an integer.

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class DequeUsingLL(object):
    def __init__(self):
        self.head = None
        self.last = None

    def add_front(self,data):
        if self.head == None:
            self.head = Node(data)
            self.last = self.head
            return
        newnode       = Node(data)
        newnode.next  = self.head
        self.head     = newnode
        


    def add_rear(self,data):
        if self.head == None:
            self.head = Node(data)
            self.last = self.head
            return
        if self.head is not None and self.head == self.last:
            self.last.next = Node(data)
            self.last      = self.last.next
        else:
            self.last.next = Node(data)
            self.last = self.last.next



    def remove_front(self):
        if not self.is_empty():

            self.head = self.head.next
        else:
            print("Deque is already empty")    
    def remove_rear(self):
        temp = self.head 
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None
        self.last = temp



    def is_empty(self):
        if self.head is None:
            return True

        return False


    def size(self):

        return 3    

    def printqueueitems(self):
        temp = self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp = temp.next
        print("\n")   


d = DequeUsingLL()
d.add_front(1)
d.add_front(2)
d.add_front(3)
d.add_rear(4)
d.add_rear(5)
d.add_rear(6)
d.printqueueitems()
d.remove_front()
d.remove_rear()
d.printqueueitems()        
isempty  = d.is_empty()
print(isempty)

d.remove_front()
d.remove_rear()
d.remove_rear()
print(isempty)
d.printqueueitems()    
d.remove_front()
print(isempty)
d.printqueueitems() 