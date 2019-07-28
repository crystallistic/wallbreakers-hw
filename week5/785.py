class Solution:
    def isBipartite(self, graph):

        # list to keep track of which group each node belongs to
        # group 0 or 1
        group = [-1 for _ in range(len(graph))]
        stack = []
        
        for node in range(len(graph)):
            if group[node] == -1:
                stack.append(node)
                group[node] = 0
            while stack: 
                node = stack.pop()

                # check all neighbors of current node
                for neighbor in graph[node]:
                    # if neighbor is not in any group 
                    if group[neighbor] == -1:
                        stack.append(neighbor)

                        # put neighbor in different group from current node
                        group[neighbor] = group[node] ^ 1
                    
                    # return False if neighbor and current node are in the same group
                    elif group[neighbor] == group[node]:
                        return False
                    
        return True