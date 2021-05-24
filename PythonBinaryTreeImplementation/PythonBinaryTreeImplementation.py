'''
Cracking the coding interview
Chapter 4 - Binary Trees
Page 100
----------------------------------------
Summary: Learning Binary Trees in Python
Constraits or Questions you need to ask:

Solution notes:

'''

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    #Helper function to print each order
    def printTree(self, traversalType):
        if traversalType == "preorder":
            return self.preOrderPrint(tree.root, "")
        elif traversalType == "inorder":
            return self.inOrderPrint(tree.root, "")
        elif traversalType == "postorder":
            return self.postOrderPrint(tree.root, "")
        else:
            print("Travesal type " + str(traversalType) + " is not supported")
            return False

    #Recursive solution to print in preorder
    def preOrderPrint(self, start, traversal):
        """Root -> Left -> Right"""
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preOrderPrint(start.left, traversal)
            traversal = self.preOrderPrint(start.right, traversal)
        return traversal

    #Recursive solution to print in inorder
    def inOrderPrint(self, start, traversal):
        """Left -> Root -> Right"""
        if start:
            traversal = self.inOrderPrint(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inOrderPrint(start.right, traversal)
        return traversal

    #Recursive solution to print in postorder
    def postOrderPrint(self, start, traversal):
        """Left -> Right -> Root"""
        if start:
            traversal = self.postOrderPrint(start.left, traversal)
            traversal = self.postOrderPrint(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal




tree = BinaryTree(1)
#        1
tree.root.left = Node(2)
tree.root.right = Node(3)
#        1
#       / \
#      2   3 
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
#         1
#       /  \
#      2    3
#     / \  / \
#    4   5 6  7 
#Pre order traversal call
# 1 - 2 - 4 - 5 - 3 - 6 - 7
print(tree.printTree("preorder"))

#In order traversal call
#4 - 2 - 5 - 1 - 6 - 3 - 7
print(tree.printTree("inorder"))

#Post order traversal call
#4 -> 5 -> 2 -> 6 -> 7 -> 3 -> 1
print(tree.printTree("postorder"))



