from collections import defaultdict
import math
class Solution:
    def networkDelayTime(self, times, N, K):
        
        neighbors = defaultdict(list)

        # record all neighbors
        for time in times:
            neighbors[time[0]].append((time[1],time[2]))
        
        path = {node:math.inf for node in range(1,N+1)}
        visited = [False for _ in range(N+1)]

        path[K] = 0
        
        while True:

            currNode = -1
            currPath = math.inf

            for i in range(1,N+1):
                
                if not visited[i] and path[i] < currPath:
   
                    currPath = path[i]
                    currNode = i
            if currNode < 0: break
            visited[currNode] = True

            for neighbor, time in neighbors[currNode]:
                path[neighbor] = min(path[currNode]+time, path[neighbor])
                    
        ans = max(path.values())
        return ans if ans < math.inf else -1

if __name__ == "__main__":
    sol = Solution()
    #times = [[2,1,1],[2,3,1],[3,4,1]]
    times = [[3,4,2],[3,5,5],[3,2,1],[3,1,7],[1,6,8],[7,3,12]]
    #times = [[1,2,1],[2,1,3]]
    
    print(sol.networkDelayTime(times, N = 7, K = 3))