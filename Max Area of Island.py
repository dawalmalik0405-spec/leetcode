grid = [
    [0, 1, 1],
    [1, 1, 0],
    [0, 1, 0]
]

visited = set()

directions = [
                (-1, 0),  # up
                (1, 0),   # down
                (0, -1),  # left
                (0, 1)    # right
            ]
max_area = 0

def dfs(row, col):
    

    if row < 0 or row >= len(grid):
        return 0

    if col < 0 or col >= len(grid[0]):
        return 0

    if grid[row][col] == 0:
        return 0

    if (row, col) in visited:
        return 0
    visited.add((row, col))
    area = 1

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        
        area += dfs(new_row, new_col)
        

    return area

def max_ar(grid):
  
  for i in range(len(grid)):
      for j in range(len(grid[0])):

          if grid[i][j] == 1 and (i,j) not in visited:
              area = dfs(i,j)
              max_area = max(max_area, area)

  return max_area


