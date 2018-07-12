#Given head of a linked list and a key, 
#delete node with this given key from the linked list.
def delete_node(head, key):
    prev = None
    current = head

    while (current != None):
        if current.data == key:
            if current == head:
                head = head.next
                current = head
            else:
                prev.next = current.next
                current = current.next
      
        else:
            prev = current
            current = current.next

    # key not found in list        
    if current == None:
        return head

    return head