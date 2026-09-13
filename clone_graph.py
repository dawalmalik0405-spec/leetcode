
from collections import deque

clones = {}
queue  = deque()



def clone(node):

    if node is None:
        return None

    clones[node] = Node(node.val)
    queue.append(node)

    while queue:

      current = queue.popleft()
      for neighbor in current.neighbors:
        if neighbor not in clones:

            clones[neighbor] = Node(neighbor.val)
            queue.append(neighbor)

        clones[current].neighbors.append(clones[neighbor])

        
    return clones[node]


       
            


















