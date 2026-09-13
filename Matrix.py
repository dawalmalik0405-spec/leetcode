from collections import deque

mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

queue = deque()

distance = [
    [-1] * len(mat[0])
    for _ in range(len(mat))
]

directions = [
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1)
]

def nearest(mat):

    for i in range(len(mat)):
        for j in range(len(mat[0])):

            if mat[i][j] == 0:
                queue.append((i, j))
                distance[i][j] = 0



    while queue:
        row, col = queue.popleft()

        for dr, dc in directions:
            new_col = col + dc
            new_row = row + dr

            if (
                0 <= new_row < len(mat) and 0<= new_col < len(mat[0])
                and distance[new_row][new_col] == -1
            ):

                distance[new_row][new_col] = distance[row][col] + 1
                queue.append((new_row, new_col))

    return distance



print(nearest(mat))






