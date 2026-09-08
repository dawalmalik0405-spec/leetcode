head = [1,2,3,4,5]
def middle_linked(head):
  slow = head
  fast = head 

  while fast and fast.next:

    slow  = slow.next
    fast  = fast.next.next  

  return slow


print(middle_linked(head))
