#Given root of a binary tree, display node values at each 
# level. Node values for all levels 
# should be displayed on separate lines.

import collections

def level_order_traversal_1(root):

    if root == None:
        return

    queues = [collections.deque(), collections.deque()]

    current_queue = queues[0]
    next_queue = queues[1]

    current_queue.append(root)
