
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


    #find an element inside the BST
    def search(self,element):
        if self.root:
            result = self._search(element,self.root)
            if result: return True
            else: return False
        else:
            print("BST is empty")

    def _search(self,element,base_node):
        if element < base_node.value and base_node.left:
            return self._search(element,base_node.left)
        elif element > base_node.value and base_node.right:
            return self._search(element,base_node.right)
        if element == base_node.value:
            return True




"""
The tree being created would look something like this
              10
       5               20
         6       12        30
                   18      
    
"""



if __name__ == '__main__':
    tree = BST()
    tree.put(10)
    tree.put(20)
    tree.put(30)
    tree.put(12)
    tree.put(18)
    tree.put(5)
    tree.put(6)


    print(tree.search(20)) #True
    print(tree.search(5))  #True
    print(tree.search(6))  #True
    print(tree.search(11)) #False
