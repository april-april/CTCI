'''
class LinkedListNode:

    def __init__(self, value):
        self.value = value
        self.next  = None


a = LinkedListNode("Angel Food")
b = LinkedListNode("Bundt")
c = LinkedListNode("Cheese")
d = LinkedListNode("Devil's Food")
e = LinkedListNode("Eccles")

a.next = b
b.next = c
c.next = d
d.next = e

# Returns the node with value "Devil's Food" (the 2nd to last node)
kth_to_last_node(2, a)

'''

def kth_to_last_node(k, head):
    # Step 1: get the length of the list
    # Start at 1, not 0
    # else we'd fail to count the head node!
    list_length = 1
    current_node = head

    # Traverse the whole list,
    # counting all the nodes
    while current_node.next:
        current_node = current_node.next
        list_length += 1

    # Step 2: walk to the target node
    # Calculate how far to go, from the head,
    # to get to the kth to last node
    how_far_to_go = list_length - k
    current_node = head
    for i in xrange(how_far_to_go):
        current_node = current_node.next

    return current_node

#Optimized solution, two pointer technique
def kth_to_last_node(k, head):
    left_node  = head
    right_node = head

    # Move right_node to the kth node
    for _ in xrange(k - 1):
        right_node = right_node.next

    # Starting with left_node on the head,
    # move left_node and right_node down the list,
    # maintaining a distance of k between them,
    # until right_node hits the end of the list
    while right_node.next:
        left_node  = left_node.next
        right_node = right_node.next

    # Since left_node is k nodes behind right_node,
    # left_node is now the kth to last node!
    return left_node