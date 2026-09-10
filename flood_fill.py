def floodFill(image, sr, sc, color):

    original_color = image[sr][sc]

    queue = [(sr,sc)]

    directions = [
        (-1, 0),
        (1, 0),
        (0, -1),
        (0, 1)
    ]

    if original_color == color:
        return image

    while queue:

        cell = queue.pop(0)
        row, col = cell 

        image[row][col] = color

        for dr, dc in directions:

            new_row = row + dr

            new_col = col + dc

            if 0 <= new_row < len(image) and 0 <= new_col < len(image[new_row]) and image[new_row][new_col] == original_color:

                image[new_row][new_col] = color
                queue.append((new_row, new_col))

    

    return image    