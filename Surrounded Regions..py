def solve(board):

    queue = []

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] == "O" and (
                i ==0 
                or i == len(board) - 1
                or j == 0
                or j == len(board)-1

            ):

                queue.append((i,j))
                board[i][j] = "S"

    while queue:
      cell = queue.pop(0)
      row, col = cell

      for dr, dc in directions:
          new_row = row + dr
          new_col = col + dc


          if (
                0 <= new_row < len(board)
                and 0 <= new_col < len(board[0])
                and board[new_row][new_col] == "O"
            ):
              board[new_row][new_col] = "S"
              queue.append((new_row, new_col))

    for i in range(len(board)):
      for j in range(len(board[0])):

          if board[i][j] == "O":
              board[i][j] = "x"
              
              # capture it

          elif board[i][j] == "S":
              board[i][j] = "O"
            # restore it

    return board


              

                      

                 
                