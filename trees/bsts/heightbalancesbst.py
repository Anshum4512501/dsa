class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None

def height(root):
    if root is None:
        return 0

    return max(height(root.left),height(root.right))+1


def isbalanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)

    if abs(lh-rh) <= 0 and (isbalanced(root.left) and isbalanced(root.right)):
        return True
    print(abs(lh-rh),root.data)    
    return False


root = Node(1)
root.right  = Node(2)
root.left = Node(3)
root.left.left = Node(4)
root.left.left.left = Node(5)



print(height(root))
print(isbalanced(root))
