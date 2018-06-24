def remove_duplicates(head):

  if head == None:
    return head

  # Let's track existing values.
  dup_set = set()
  
  dup_set.add(head.data)
  curr = head

  while curr.next != None:
    if curr.next.data in dup_set:
      # Duplicate node found. Let's remove it from the list.
      curr.next = curr.next.next
    else:
      # Element not found in map, let's add it.
      dup_set.add(curr.next.data)
      curr = curr.next

  return head