# import 
    

# FINDIN MINIMUM IN BST
class BSTMINIMUM(BST):
    def minimum(self,node):
        parent = None
        while node:
            parent = node
            node = node.left
        return parent.data    



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

bst.in_order(bst.root)
bstmin  = BSTMINIMUM()
print("\n",bstmin.minimum(bst.root))