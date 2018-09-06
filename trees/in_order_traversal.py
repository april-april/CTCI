import collections

def inorder_iterative(root):
    if root == None:
        return

    stack = collections.deque()
    count = 0

    while (len(stack) != 0 or root != None):
        if root != None:
            stack.append(root)
            root = root.left
            continue

            
        print str(stk[-1].data) + " ",
        root = stack[-1].right
        stack.pop()

def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())

