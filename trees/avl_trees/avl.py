class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.left = None
        self.right = None
        self.height = 0

class AVLTree:
    def __init__(self) -> None:
        self.root = None


    def insert(self,data):
        newnode = Node(data)
        
        # if self.root == None:
        #     self.root = newnode
        #     self.root.height = newnode.height + 1
        #     return
        # # temp = self.root
        # parent = None
        # while temp:
        #     if data < temp.data:
        #         parent = temp
        #         parent.height += 1
        #         temp = temp.left
        #     else:
        #         parent = temp
        #         parent.height += 1
        #         temp = temp.right 

        # if data < parent.data:
        #     parent.left = newnode
            

        # else:
        #     parent.right = newnode
            
    def insert_util(self,newnode,root):
        if root == None:
            return newnode
        if newnode.data > root.data:
            root.right = self.insert_util(self,newnode,root.right)
        elif newnode.data < root.data:
            root.left = self.insert_util(self,newnode,root.left)

        self.height = self.get_height(root)  


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




