from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        # failed attempt at dfs
        '''def isLand(x, y):
            return (0 <= x < m) and (0 <= y < n) and (grid[x][y] == 1)

        def onEdge(x, y):
            return (grid[x][y] == 2) or (x == 0) or (x == m-1) or (y == 0) or (y == n-1)

        def enclaveify(x, y, fromEdge):
            if fromEdge or onEdge(x, y):
                fromEdge = True
                grid[x][y] = 2

            for dx, dy in directions:
                newX, newY = x + dx, y + dy
                if isLand(newX, newY) and (newX, newY) not in seen:
                    seen.add((newX, newY))
                    fromEdge = enclaveify(newX, newY, fromEdge)
                    if fromEdge:
                        grid[x][y] = 2

            return fromEdge
        
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # u, d, l, r
        seen = set()
        
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in seen:
                    seen.add((x, y))
                    enclaveify(x, y, False)

        print(grid)

        enclaves = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    enclaves += 1

        return enclaves'''

        # new attempt using bfs
        '''def onGrid(x, y):
            return 0 <= x < m and 0 <= y < n

        # find out how much land is part of an enclave
        # return 0 if we find out the enclave is actually a peninsula
        def traverseLand(x, y):
            q = deque()
            seen.add((x, y))
            q.append((x, y))

            area = 0
            isPeninsula = False
            while len(q) > 0:
                cx, cy = q.popleft()
                area += 1

                for dx, dy in directions:
                    newX, newY = cx + dx, cy + dy

                    if onGrid(newX, newY):
                        if grid[newX][newY] == 1 and (newX, newY) not in seen:
                            seen.add((newX, newY))
                            q.append((newX, newY))
                    else:
                        # we still want to check all possible land in order
                        # to avoid falsely claiming some land as an enclave
                        isPeninsula = True

            if isPeninsula:
                return 0
            return area

        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # u, d, l, r
        seen = set()

        enclaveArea = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1 and (x, y) not in seen:
                    enclaveArea += traverseLand(x, y)
                    
        return enclaveArea'''

        # retry attempt at dfs
        # goal is to tag all peninsula-related land and then count enclaves' area
        def isLand(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == 1
        
        def traversePeninsula(x, y):
            grid[x][y] = 2 # tag peninsula on the grid

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                # we don't need 'seen'. handled by tagging already
                '''if isLand(nx, ny) and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    traversePeninsula(nx, ny)'''
                if isLand(nx, ny):
                    traversePeninsula(nx, ny)

        
        m = len(grid)
        n = len(grid[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] # u, d, l, r
        # seen = set()

        # a peninsula only originates from the edges of the grid.
        # perform dfs from land connected to the edges
        
        # first, the top and bottom rows
        for c in range(n):
            if grid[0][c] == 1:
                traversePeninsula(0, c)
            
            if grid[m-1][c] == 1:
                traversePeninsula(m-1, c)
        
        # then, the left and right columns
        for r in range(m):
            if grid[r][0] == 1:
                traversePeninsula(r, 0)
            
            if grid[r][n-1] == 1:
                traversePeninsula(r, n-1)

        # finally, sum the areas of all enclaves
        area = 0
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    area += 1

        return area


        

sol = Solution() 
print(sol.numEnclaves([
    [0,1,0,1,0,1,1,0,1,0,0,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,1,1,0,1,1,0,0,1,0,0,0,1,0,1,1,1,1,0,1,0,0,0,1,0], 
    [1,0,1,0,0,1,1,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,1,1,0,0,0,1,0,0,0,0,0,1,1,1,0,1,0,1,1,0,0,0,0,1,0,0,0,1],
    [0,0,0,1,1,0,0,0,1,0,0,1,1,1,1,0,1,0,0,1,0,1,0,0,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0,1,1,1,0,0,0,0,1,1,0,0], 
    [1,1,0,1,1,1,0,0,1,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,1,1,0,0,0,0,0,0,1,1,0,0,0,1,1,1,1,1,0,1,1,0,1],
    [0,1,1,1,0,0,0,1,0,0,0,1,1,0,0,1,0,0,0,1,1,0,0,1,1,0,1,0,0,0,0,0,1,0,1,1,0,1,0,0,0,1,1,0,1,0,0,0,0,1], 
    [1,0,0,0,0,0,0,1,0,1,1,0,0,0,1,0,0,0,1,0,1,1,0,1,1,0,1,0,0,1,1,0,1,1,1,0,0,0,0,0,1,1,0,1,0,0,1,1,0,1],
    [0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,0,0,1,0], 
    [1,0,0,1,0,1,0,0,0,0,0,0,1,0,1,0,1,0,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,0,1,1,1,1,1,0,1,0,1,0,1,0,0,0,0,0],
    [0,0,0,1,0,1,0,0,1,0,1,0,0,1,1,0,0,0,0,0,1,1,0,1,1,1,0,0,1,0,1,1,0,0,1,1,0,1,1,0,1,0,0,0,1,0,0,0,1,0],
    [1,1,0,0,0,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,0,1,0,0,0,0,1,0,1,1,1,0,1,1,0,0]
]))