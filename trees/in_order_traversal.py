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

        root = stack[-1].right
        stack.pop()