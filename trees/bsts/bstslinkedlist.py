class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self,data):
        newnode = Node(data)
        temp = self.root
        if self.root is None:
            self.root = newnode
            return
        while temp is not None:
            if temp.data < newnode.data:
                parentnode = temp
                temp = temp.right

            elif temp.data > newnode.data:
                parentnode = temp
                temp = temp.left

        if parentnode.data > newnode.data:
            parentnode.left = newnode
        else : 
            parentnode.right = newnode    

    def inorder(self,node):
        if node == None:
            
            return
        self.inorder(node.left)
        print(node.data,end=" ") 
        self.inorder(node.right) 
    def preorder(self,node):
        if node == None:
            
            return
        print(node.data,end=" ") 
        self.preorder(node.left)
        self.preorder(node.right)                      


bst = BST()
bst.insert(1)
bst.insert(2)
bst.insert(6)
bst.insert(4)
bst.insert(5)
bst.insert(8)

bst.inorder(bst.root)
print("\n")
bst.preorder(bst.root)
