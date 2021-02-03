class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,key):
        newnode = Node(key)
        q = []
        if self.root is None:
            self.root = newnode
            q.append(self.root)
            return
        
        while len(q):
            temp = q.pop(0)

            if not temp.left:
                temp.left = newnode
                break
            else:
                q.append(temp.left)

            if not temp.right:
                temp.right = newnode
                break
            else:
                q.append(temp.right)

    def inorder(self,node):
        if node == None:
            return
        self.inorder(node.left)
        print(node.data) 
        self.inorder(node.right)


   
        




            






        
t = Tree()
t.insert(1)
t.insert(2)
t.insert(3)
t.inorder(t.root)
