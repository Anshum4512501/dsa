class Node:
    def __init__(self,data) -> None:
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self,data):
        newnode = Node(data)
        parent = None
        if self.root == None:
            self.root = newnode
            return 
        temp = self.root
        parent = None
        while temp:
            if temp.data < data:
                parent = temp
                temp = temp.right

            elif temp.data>data:
                parent = temp
                temp = temp.left

        if parent.data > data :
            parent.left = newnode
        else:
            parent.right = newnode  

    def inorder(self,node):
        if node:

            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
            



    def preorder(self,node):
        
        if node:
            print(node.data,end=" ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self,node):
        
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data,end=" ")
def inorder(node):
    if node:

        inorder(node.left)
        
        inorder(node.right)

def bst_to_heap(root):
    if root is None:
        return None


bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.insert(6)
print("\ninorder")
bst.inorder(bst.root)
print("\npreorder")
bst.preorder(bst.root)
print("\npostorder")
bst.postorder(bst.root)