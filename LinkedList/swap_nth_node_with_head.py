# Node indices starts from 1.
def swap_nth_node(head, n):
    prev = None
    current = head

    if head == None:
        return head

    if n == 1:
        # No need to swap head with head.
        return head
    
    count = 1

    while current != None and count < n:
        prev = current
        current = current.next
        count += 1

    if current == None:
        return head
    
    # current is pointing to nth node

    prev.next = head
    temp = head.next
    head.next = current.next
    current.next = temp

    return current