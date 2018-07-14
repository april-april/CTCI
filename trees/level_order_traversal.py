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
    level_number = 0

    while current_queue:
        temp = current_queue.popleft()
        print str(temp.data) + " ",

        if temp.left != None:
            next_queue.append(temp.left)

        if temp.right != None:
            next_queue.append(temp.left)

        if not current_queue:
            print
            level_number += 1
            current_queue = queues[level_number % 2]
            next_queue = queues[(level_number + 1) % 2]
    
    print

