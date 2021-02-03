bst = [None]*100

def root(key):
    if bst[0] is not None:
        print("root is already there")
        return
    bst[0] = key
    return    


def insert(root,key):
    if root is None or key is None:
        return

    if key < root[0]:
        # leftchild = index(root)*2 + 1
        
        # return insert(root)   
        pass 


def inorder(root):
    pass
