tree = [None]*100

def root(key):
    if tree[0] is not None:
        print("Root is already there")
        return
    tree[0] = key
    return

def setleft(key,parent):
    if parent is None or key is None:
        return
    left = parent*2 + 1
    tree[left] = key


def setright(key,parent):
    if parent is None or key is None:
        return
    right = parent*2 + 2
    tree[right] = key

def printtree(root):
    if root is None:
        return 
    lengthoftree = len(tree)
    for element in range(lengthoftree):
        if tree[element]:
            print(tree[element],end=" ")
        else:
            print("_",end=" ")            
    

root("A")
setleft("B",0)
setleft("C",1)
setleft("D",3)
setleft("E",7)
setleft("F",15)

printtree(0)