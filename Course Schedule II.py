from collections import deque

class Solution(object):
    def findOrder(self, numCourses, prerequisites):

        queue = deque()
        order = []
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            current = queue.popleft()

            order.append(current)

            for neighbor in graph[current]:
                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        if len(order) == numCourses:
            return order
        return []



