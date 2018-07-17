import collections

def inorder_iterative(root):
    if root == None:
        return

    stack = collections.deque()
    count = 0

    while (len(stk) != 0 or root != None): 