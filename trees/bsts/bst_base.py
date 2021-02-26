class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.right = None
        self.data = data
class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self,data):
        newnode = Node(data)
        if self.root == None:
            self.root = newnode
            return 

        temp = self.root 
        parent = None
        while temp:
            if temp.data < data:
                parent = temp
                temp = temp.right
            else:
                parent = temp
                temp = temp.left

        if parent.data < data :
            parent.right = newnode
        else:
            parent.left = newnode
            
    def in_order(self,root):
        if root:
            self.in_order(root.left)
            print(root.data,end=" ")
            self.in_order(root.right)