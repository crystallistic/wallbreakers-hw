from collections import deque, defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:       
        
        """ Using Kahn's Topological Sorting algorithm"""
        neighbors = defaultdict(list)
        # calculate in-degree
        inDegree = [0 for _ in range(numCourses)]
        for edge in prerequisites:
            inDegree[edge[1]] += 1
            neighbors[edge[0]].append(edge[1])
        
        # queue
        queue = deque()
        for node, deg in enumerate(inDegree):
            if deg == 0:
                queue.append(node)
        
        # count of visited nodes
        visited = 0
        while queue:
            node = queue.popleft()
            visited += 1

            # loop through all neighbors of a node and reduce their 
            # in-degrees, if reduced to 0 then add node to queue
            for neighbor in neighbors[node]:
                inDegree[neighbor] -= 1
                if inDegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return visited == numCourses