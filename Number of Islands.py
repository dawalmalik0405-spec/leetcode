

def  number_of_island(island):
  visited = set()
  count = 0
  queue = []
  directions = [
                (-1, 0),  # up
                (1, 0),   # down
                (0, -1),  # left
                (0, 1)    # right
            ]

  for i in range(len(island)):
    for j in range(len(island[i])):

      if (i,j) not in  visited and island[i][j] == 1:
        count += 1

        visited.add((i,j))

        queue.append((i,j))

        while queue:
          cell = queue.pop(0)
          row, col = cell

          

          for dr, dc in directions:

            new_row = row + dr
            new_col = col + dc

            if 0 <= new_row < len(island) and 0 <= new_col < len(island[new_row]) and island[new_row][new_col] == 1 and (new_row,new_col) not in visited:

              visited.add((new_row,new_col))
              queue.append((new_row, new_col))

  return count





