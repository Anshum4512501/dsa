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
        if self.root == None:
            self.root = newnode
            return
        temp = self.root
        parent = None

        while temp:
            if temp.data < data:
                parent = temp
                temp = temp.right
            elif temp.data > data:
                parent = temp
                temp = temp.left
        
        if parent.data > data :
            parent.left = newnode
        elif parent.data < data:
            parent.right = newnode

    def search(self,data):
        temp = self.root    
        while temp:

            if data is None:
                return False
            if data == temp.data:
                return temp

            if temp.data < data:
                temp = temp.right
            elif temp.data > data:
                temp  = temp.left    
            if temp is None:
                return False    

    def leftmost(self,node):
        if not node:
            return None
        while node:
            parent = node
            node = node.left
        return parent     
    def rightmost(self,node):
        while node:
            parent = node
            node = node.right
        return parent

    def predecessor(self,data):
        temp = self.root
        if data == temp.data:
            node = self.rightmost(temp.left)
            return node.data
        if data >= temp.data:
            return temp.data    

    def sucessor(self,data):
        temp = self.root
        if data == temp.data:
            node = self.leftmost(temp.right)
            return node.data
        if data <= temp.data:
            return temp.data  





    def inorder(self,node):
        if node == None:
            
            return
        self.inorder(node.left)
        print(node.data,end=" ") 
        self.inorder(node.right) 

bst = BST()
bst.insert(15)
bst.insert(24)
bst.insert(59)
bst.insert(6)
bst.insert(10)
bst.insert(9)
bst.insert(23)
bst.insert(21)
bst.insert(12)
bst.insert(7)
bst.insert(8)
bst.insert(13)

bst.inorder(bst.root)        
sucessor = bst.sucessor(5)
print("sucessor",sucessor)