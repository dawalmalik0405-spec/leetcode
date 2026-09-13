from collections import deque

numCourses = 2
prerequisites = [[1,0]]

def canFinish(numCourse, prequisites):

  queue = deque()

  graph = [[] for _ in range(numCourse)]

  indegree = [0] * numCourse

  for course, prequisit in prequisites:
    graph[prequisit].append(course)
    indegree[course] += 1

  for i in range(numCourse):
    if indegree[i] == 0:
      queue.append(i)

  while queue:
    current = queue.popleft()
    course_taken += 1

    for neighbor in graph[current]:
      indegree[neighbor] -= 1

      if indegree[neighbor] == 0:
          queue.append(neighbor)

  return course_taken == numCourse

    







