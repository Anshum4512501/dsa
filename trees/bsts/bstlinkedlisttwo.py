class Node:
    def __init__(self,data):
        self.left  = None
        self.data  = data
        self.right = None


class BST:

    def insert(self, root, key): 
        # Step 1 - Perform normal BST 
        if not root: 
            return Node(key) 
        elif key < root.data: 
            root.left = self.insert(root.left, key) 
        else: 
            root.right = self.insert(root.right, key) 

        return root
    
    def inorder(self,root):
        if not root: 
           return
        self.inorder(root.left)
        print("{0} ".format(root.data), end="") 
         
        self.inorder(root.right) 

root = None
bst = BST()  
root = bst.insert(root, 10) 
root = bst.insert(root, 20) 
root = bst.insert(root, 30) 
root = bst.insert(root, 40) 
root = bst.insert(root, 50) 
root = bst.insert(root, 25) 
bst.inorder(root)                  