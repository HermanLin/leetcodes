
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def isIsland(x, y):
            return (0 <= x < m) and (0 <= y < n) and (grid[x][y] == 1)
        
        # use DFS to discover the entirety of an island and its area
        def dfs(x, y) -> int:
            area = 1
            for dx, dy in directions:
                nextX, nextY = x + dx, y + dy
                if isIsland(nextX, nextY) and (nextX, nextY) not in seen:
                    seen.add((nextX, nextY))
                    area += dfs(nextX, nextY)
                    
            return area
        
        m = len(grid)
        n = len(grid[0])
        
        # dictate possible directional movements
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        
        max_area = 0
        seen = set()
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in seen:
                    seen.add((x, y))
                    area = dfs(x, y)
                    max_area = max(max_area, area)
                    
        return max_area

        '''# if we're allowed to modify the input grid
        def dfs(x, y) -> int:
            grid[x][y] = 2

            area = 1
            for dx, dy in directions:
                nextX, nextY = x + dx, y + dy
                if isIsland(nextX, nextY):
                    area += dfs(nextX, nextY)

            return area
        
        max_area = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    area = dfs(x, y)
                    max_area = max(max_area, area)

        return max_area'''

sol = Solution() 
print(sol.maxAreaOfIsland([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))
print(sol.maxAreaOfIsland([[0,0,0,0,0,0]]))