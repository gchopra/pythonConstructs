
#create a node for th binary tree
class node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

#create the tree using nodes
class binaryTree:
    def __init__(self,root):
        self.root = node(root)


    #Pre order traversal: root node -> left node -> right node
    #In the sequence every node end up printing in the form of base node
    def preOrderTraversal(self,base_node,travel_path):
        if base_node:
            travel_path += str(base_node.value) + '-'
            travel_path = self.preOrderTraversal(base_node.left,travel_path)
            travel_path = self.preOrderTraversal(base_node.right,travel_path)
        return travel_path

    #In order traversal: left node -> root node -> right node
    def inOrderTraversal(self,base_node,travel_path):
        if base_node:
            travel_path = self.inOrderTraversal(base_node.left,travel_path)
            travel_path += str(base_node.value) + '-'
            travel_path = self.inOrderTraversal(base_node.right,travel_path)
        return travel_path

    def postOrderTraversal(self,base_node,travel_path):
        if base_node:
            travel_path = self.postOrderTraversal(base_node.left,travel_path)
            travel_path = self.postOrderTraversal(base_node.right,travel_path)
            travel_path += str(base_node.value) + '-'
        return travel_path


"""
The tree being created would look something like this
              10
       20            30
    40    50       60   70

pre order sequence = 10-20-40-50-30-60-70-
in order sequence = 40-20-50-10-60-30-70-
post order sequence = 40-50-20-60-70-30-10-
"""

if __name__ == '__main__':
    tree = binaryTree(10)

    tree.root.left = node(20)
    tree.root.right = node(30)

    tree.root.left.left = node(40)
    tree.root.left.right = node(50)

    tree.root.right.left = node(60)
    tree.root.right.right = node(70)

    print(tree.preOrderTraversal(tree.root,""))
    print(tree.inOrderTraversal(tree.root, ""))
    print(tree.postOrderTraversal(tree.root, ""))