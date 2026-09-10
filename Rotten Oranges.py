def orangesRotting(grid):

    queue = []
    fresh = 0
    minutes = 0

    directions = [
                    (-1, 0),  # up
                    (1, 0),   # down
                    (0, -1),  # left
                    (0, 1)    # right
                ]

    # scan the grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):

            if grid[i][j] == 2:
                queue.append((i, j))

            if grid[i][j] == 1:
                fresh += 1

    while queue and fresh > 0:
        number_of_rotten = len(queue)

        for i in range(number_of_rotten):
            cell = queue.pop(0)

            row, col = cell
            
                      
            
            for dr, dc in directions:
  
              new_row = row + dr
              new_col = col + dc
  
              if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]) and grid[new_row][new_col] == 1:

                  grid[new_row][new_col] = 2
                  fresh -= 1                         
                  queue.append((new_row,new_col))

            minutes += 1

    if fresh > 0:
      return -1

    return minutes

    
