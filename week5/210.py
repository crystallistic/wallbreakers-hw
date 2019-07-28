from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        """ Using Kahn's Topological Sorting algorithm"""
        neighbors = defaultdict(list)
        # calculate in-degree
        inDegree = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            inDegree[edge[0]] += 1
            neighbors[edge[1]].append(edge[0])
        
        # queue
        queue = deque()
        for node, deg in enumerate(inDegree):
            if deg == 0:
                queue.append(node)
        
        order =[]
        visited = 0
        while queue:
            node = queue.popleft()
            order.append(node)
            visited += 1

            for neighbor in neighbors[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
       
        return order if visited == numCourses else []