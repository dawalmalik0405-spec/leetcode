

def linked_cycle_list(head):

  current = head

  visited = {}


  while current:
    if current in visited:
      return True

    visited[current] = current

    current = current.next

  return False




