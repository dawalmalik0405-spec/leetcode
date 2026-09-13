
from collections import deque

clones = {}
queue  = deque()
directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]


def clone(node):
  for neighbor in node.neighbors:

    if neighbor not in clones:

      clones[node] = node(node.val)
      queue.append(node)

      while queue:

        current = 0

        row, col = queue.popleft()
        
        for dr, dc in directions:
            new_col = col + dc
            new_row = row + dr
            


















