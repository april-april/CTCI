from LinkedList import LinkedList
# delete middle node by copying contents of next node to middle/current
# node. The next node will be deleted after contents of next node are 
# copied over to middle node.

def delete_middle_node(node):
    node.value = node.next.value
    node.next = node.next.next