#Here we will check if the Tree satisfies BST property
#We check this property using the in oreder traversal
#create a node for the binary search tree
class node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

#create the tree using nodes
class BST:
    def __init__(self):
        self.root = None


    #insert elements into the BST
    def put(self,val):
        if self.root is None:
            self.root = node(val)
        else:
            self._put(val,self.root) #starting from root, find the right place to put value

    def _put(self,val,base_node):
        if val < base_node.value:
            if base_node.left is None:
                base_node.left = node(val) #keep going till you find a place to put
            else:
                self._put(val,base_node.left)
        elif val > base_node.value:
            if base_node.right is None:
                base_node.right = node(val) #keep going till you find a place to put
            else:
                self._put(val,base_node.right)

        else:
            print ("Duplicate value not allowed")

    #In order traversal: left node -> root node -> right node
    def inOrderTraversal(self,base_node,travel_path):
        if base_node:
            travel_path = self.inOrderTraversal(base_node.left,travel_path)
            travel_path += str(base_node.value) + '-'
            travel_path = self.inOrderTraversal(base_node.right,travel_path)
        return travel_path


    def propertyCheck(self):
        if self.root:
            result = self._propertyCheck(self.root)
            if result is None : return True
            else: return False
        else:
            print("Empty Tree")

    def _propertyCheck(self,base_node):
        if base_node.left:
            if base_node.value > base_node.left.value:
                return self._propertyCheck(base_node.left)
            else: return False
        if base_node.right:
            if base_node.value < base_node.right.value:
                return self._propertyCheck(base_node.right)
            else: return False


if __name__ == '__main__':
    tree = BST()
    tree.put(10)
    tree.put(20)
    tree.put(30)
    tree.put(12)
    tree.put(18)
    tree.put(5)
    tree.put(6)

    random_tree = BST()
    random_tree.root = node(1)
    random_tree.root.left = node(2)
    random_tree.root.right = node(3)

    print(tree.inOrderTraversal(tree.root,""))
    print(tree.inOrderTraversal(random_tree.root,""))

    print(tree.propertyCheck()) #True
    print(random_tree.propertyCheck())  #False