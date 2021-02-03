# push(element)
# pop()
# isempty()
# peek()

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def push(self,element):
        newnode = Node(element)
        newnode.next = self.head
        self.head = newnode
        

    def pop(self):
        if self.isempty():
            return float("-inf")
        self.head = self.head.next    
        

    def isempty(self):
        if self.head == None:
            return True
        return False    

    def peek(self):
        return self.head.data

    def printstack(self):
        last = self.head 
        while last:
            print(last.data,end=" ")
            last = last.next

stack = Stack()
print(stack.isempty())

stack.push(1)
stack.push(2)
stack.push(3)

stack.printstack()

print("\n",stack.isempty())
stack.pop()

stack.printstack()
