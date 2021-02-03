import random
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode = Node(data)
            newnode.next = self.head    
            self.head = newnode

    def printll(self):
        last = self.head 
        while last:
            print(last.data , end=" ")
            last = last.next

    def find_length_of_ll(self):
        if self.head == None:
            return 0
        last = self.head
        count = 0 
        while last :
            count += 1 
            last = last.next    
        return count    

    def rotate_by_k(self,k):
        length = self.find_length_of_ll()
        print("length = {}".format(length))
        if length == 0:
            return 
        temp = self.head
        previous = None
        while k and k <= length:
            previous = temp
            temp = temp.next
            k = k-1
        if temp is not None:
            temp.next = self.head
            previous.next = None




ll = LinkedList()
l =  [i for i in range(2,1000,70)]
for item in l:
    ll.push(random.choice(l))
ll.printll()
ll.rotate_by_k(2)
print("\n")
ll.printll()