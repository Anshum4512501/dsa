class Node:
    def __init__(self,data):
        self.left = None
        self.data = data
        self.right = None


class BST:
    def __init__(self) -> None:
        self.root = None


    def insert(self,data):
        newnode  = Node(data)
        if self.root == None:
            self.root = newnode
            return

        temp = self.root 
        parent = None

        while temp:
            if data < temp.data:
                parent = temp
                temp  = temp.left
            else :
                parent = temp
                temp = temp.right

        if parent.data<data:
            parent.right = newnode
        else:
            parent.left = newnode

    def find_node(self,data):
        temp = self.root
        node = self.search_utils(temp,data)
        return node
        
    def search_utils(self,node,data):
        if node.data == data:
            return node
        if node.data < data:
            return self.search_utils(node.right,data)    
        return self.search_utils(node.left,data)
    def inorder(self,node):
        if node:
            self.inorder(node.left)
            print(node.data,end=" ")
            self.inorder(node.right)
    def minimum(self,node):
        temp = node
        while temp.left:
            temp = temp.left
        return temp    

    def maximum(self,node):
        temp = node
        while temp.right:
            temp = temp.right

        return temp



    def find_successor(self,data):
        node = self.find_node(data)
        if node.right != None:
            return self.minimum(node)

        return self.find_successor_util(node)    

    def find_parent_of_node(self,node):
        temp = self.root
        parent = None
        if temp.data == node.data:
            parent = node
            return parent
        while temp.data != node.data:
            if temp.data<node.data:
                parent = temp
                temp = temp.right
            else:
                parent = temp
                temp = temp.left

        return parent            
                  
    def find_successor_util(self,node):
        temp = self.root
        
        pass        
                
    def number_of_children(self,node_to_be_deleted):
        if node_to_be_deleted.left != None:
            if node_to_be_deleted.right!= None:
                return 2
            return 1
        if node_to_be_deleted.left == None:
            if node_to_be_deleted.right!= None:
                return 1    

        return 0    

    def delete(self,data):
        node_to_be_deleted = self.find_node(data)
        parent = self.find_parent_of_node(node_to_be_deleted)

        if not node_to_be_deleted:
            print("No node found")
            return

        if self.number_of_children(node_to_be_deleted) == 0:
            
            if parent.right == node_to_be_deleted:
                parent.right = None
            else:
                parent.left = None
        if self.number_of_children(node_to_be_deleted) == 1:
            
            if parent.right == node_to_be_deleted:
                parent.right = node_to_be_deleted.right
            else:
                parent.left = node_to_be_deleted.left

        else:
            sucessor = self.minimum(node_to_be_deleted)

            if parent.right == node_to_be_deleted:
                
                sucessor.left = node_to_be_deleted.left
                sucessor.right = node_to_be_deleted.right
                parent.right = sucessor
            else:
                sucessor.left = node_to_be_deleted.left
                sucessor.right = node_to_be_deleted.right
                parent.left = sucessor






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
serched_element = bst.find_node(7)

print("\nserched_element",serched_element)

bst.delete(18)
bst.inorder(bst.root)