

def intersect(n1, n2):

  l1 = len(n1)
  l2 = len(n2)

  t_l = abs(l1 - l2)
  p1 = n1
  p2 = n2

  

  if l1 > l2:
    for _ in range(t_l):
      p1 = p1.next
  else:
    for _ in range(t_l):
      p2 = p2.next

  while p1 is not p2:
    p1 = p1.next
    p2 = p2.next

  return p1

