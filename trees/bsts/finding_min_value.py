class Node:
    def __init__(self,data) -> None:
        self.left  = None
        self.data  = data
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
        parent = temp
        while temp:
            if temp.data > data:
                parent = temp
                temp = temp.left
            elif temp.data < data:
                parent = temp
                temp = temp.right

        if parent.data > data :
            parent.left = newnode
        else:
            parent.right = newnode                

    def find_min(self):
        temp  = self.root
        parent = None
        while temp:
            parent = temp
            temp = temp.left

            if not parent.left:
                print("least element in bst is {}".format(parent.data))
                return parent.data                        


bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(4)
bst.insert(2)
bst.insert(6)

bst.find_min()