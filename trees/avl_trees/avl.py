class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self) -> None:
        self.root = None


    def insert(self,data):
        newnode = Node(data)
        newnode.height = 0
        if self.root == None:
            self.root = newnode
            self.root.height = 1
            return
        temp = self.root
        parent = None
        while temp:
            if data < temp.data:
                parent = temp
                temp = temp.left
            else:
                parent = temp
                temp = temp.right 

        if data < parent.data:
            parent.left = newnode
            parent

        else:
            parent.right = newnode

    def get_height(self,root):
        pass

    def get_balancing_factor(self,node):
        pass

    def left_rotate(self,node):
        pass

    def right_rotate(self,node):
        pass
    
           

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)   




