class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None


def insert(root,key):
    if root is None:
        return Node(key)

    if root.data == key:
        return root

    if root.data < key:
        root.right = insert(root.right,key)
    elif root.data > key :
        root.left = insert(root.left,key)


    return root

r = Node(1)
insert(r,3)