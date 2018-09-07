# A class that represents an individual node in a
# Binary Tree
class Node:

	def __init__(self,key):
		self.left = None
		self.right = None
		self.val = key

# A function to do inorder tree traversal
def printInorder(root):

	if root:
		# First recur on left child
		printInorder(root.left)

		# then print the data of node
		print(root.val),

		# now recur on right child
		printInorder(root.right)

#Python book version
def inorder(tree):

    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())

# A function to do postorder tree traversal
def printPostorder(root):

	if root:
		# First recur on left child
		printPostorder(root.left)

		# the recur on right child
		printPostorder(root.right)

		# now print the data of node
		print(root.val)

#book variation
def postorder(tree):

    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())

# preorder tree traversal
def printPreorder(root):

	if root:
		# First print the data of node
		print(root.val),

		# Then recur on left child
		printPreorder(root.left)

		# Finally recur on right child
		printPreorder(root.right)

# book variation
def preorder(self):

    print(self.key)
    if self.leftChild:
        self.leftChild.preorder()
    if self.rightChild:
        self.rightChild.preorder()





