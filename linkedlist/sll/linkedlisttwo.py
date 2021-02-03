#inserting elements in linked list at the end 

class Node :

    def __init__(self,data):
        self.data = data 
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None 

    def insertatbegining(self,data):
        
        newnode = Node(data)
        if self.head == None:
            self.head = newnode
            return
        newnode.next = self.head   
        self.head = newnode
        

    def printlist(self):
        temp = self.head
        while temp:
            print(temp.data,end="")
            temp = temp.next



l = LinkedList()
l.insertatbegining(1)
l.insertatbegining(2)
l.insertatbegining(3)
l.printlist()