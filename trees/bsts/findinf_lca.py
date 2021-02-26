class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

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
            if data < temp.data:
                parent = temp
                temp = temp.left
            else:
                parent = temp
                temp = temp.right 

        if data < parent.data:
            parent.left = newnode

        else:
            parent.right = newnode

    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)

    def least_common_ancester(self,root,node_one,node_two):
        if root.data > node_one and root.data > node_two:
            return self.least_common_ancester(root.left,node_one,node_two)
        elif root.data < node_one and root.data < node_two:
            return self.least_common_ancester(root.right,node_one,node_two)
        else:
            print("\nlca is",root.data)
            return root
bst = BST()
bst.insert(15)
bst.insert(6)
bst.insert(18)
bst.insert(3)
bst.insert(7)
bst.insert(17)
bst.insert(20)
bst.insert(2)
bst.insert(4)
bst.insert(13)
bst.insert(9)
bst.inorder(bst.root)            
lca = bst.least_common_ancester(bst.root,3,9)
