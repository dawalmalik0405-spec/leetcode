def reverseList(self, head):
    previous = None
    current = head

    while current:
        next_node = current.next_node

        current.next_node = previous 

        previous = current 

        current = next_node
        # write the 4 operations

    return previous