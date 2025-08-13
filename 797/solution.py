from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(path):
            # the last node in our path should be N-1
            if path[-1] == N - 1:
                ans.append(path[:])
                return
            
            neighbors = graph[path[-1]]
            for n in neighbors:
                path.append(n)
                dfs(path)
                path.pop()
                
            
        N = len(graph)
        ans = []
        dfs([0])
        return ans

sol = Solution() 
print(sol.allPathsSourceTarget([[1,2],[3],[3],[]]))
print(sol.allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
