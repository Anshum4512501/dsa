class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def insert(root,key):
    if root is None:
        return  Node(key)

    if root.data == key:
        return root
    if root.data < key: 
        root.right = insert(root.right, key) 
    else: 
        root.left = insert(root.left, key)         

    return root

def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.data,end=" ") 
    inorder(root.right)


r = Node(50) 
r = insert(r, 30) 
r = insert(r, 20) 
r = insert(r, 40) 
r = insert(r, 70) 
r = insert(r, 60) 
r = insert(r, 80) 
  
# Print inoder traversal of the BST 
inorder(r)            