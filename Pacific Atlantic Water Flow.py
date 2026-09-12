from collections import deque

class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        rows = len(heights)
        cols = len(heights[0])

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        pacific = set()
        atlantic = set()

        pacific_queue = deque()
        atlantic_queue = deque()

        # Pacific: top row + left column
        for col in range(cols):
            pacific.add((0, col))
            pacific_queue.append((0, col))

        for row in range(rows):
            pacific.add((row, 0))
            pacific_queue.append((row, 0))

        # Atlantic: bottom row + right column
        for col in range(cols):
            atlantic.add((rows - 1, col))
            atlantic_queue.append((rows - 1, col))

        for row in range(rows):
            atlantic.add((row, cols - 1))
            atlantic_queue.append((row, cols - 1))

        def bfs(queue, visited):

            while queue:

                row, col = queue.popleft()

                for dr, dc in directions:

                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and (new_row, new_col) not in visited
                        and heights[new_row][new_col] >= heights[row][col]
                    ):
                        visited.add((new_row, new_col))
                        queue.append((new_row, new_col))

        # Find cells that can reach Pacific
        bfs(pacific_queue, pacific)

        # Find cells that can reach Atlantic
        bfs(atlantic_queue, atlantic)

        # Cells reachable from both oceans
        result = []

        for row, col in pacific:
            if (row, col) in atlantic:
                result.append([row, col])

        return result