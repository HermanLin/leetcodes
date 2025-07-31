from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        def valid(x, y) -> bool:
            return (0 <= x < m) and (0 <= y < n) and (maze[x][y] == ".")
        
        '''def isExit(x, y) -> bool:
            notStart = not (x == entrance[0] and y == entrance[1])
            atTop = (x == 0)
            atBottom = (x == m - 1)
            atLeft = (y == 0)
            atRight = (y == n - 1)
            
            return notStart and (atTop or atBottom or atLeft or atRight)
        
        m = len(maze)
        n = len(maze[0])
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        seen = {(entrance[0], entrance[1])}
        # store the number of steps we take along with the node
        queue = deque([(entrance[0], entrance[1], 0)])
        
        while queue:
            x, y, steps = queue.popleft()
            
            if isExit(x, y):
                return steps
            
            for dx, dy in directions:
                newX, newY, newS = x + dx, y + dy, steps + 1
                if valid(newX, newY) and (newX, newY) not in seen:
                    seen.add((newX, newY))
                    queue.append((newX, newY, newS))
                    
        return -1'''

        # improved solution if allowed to modify input
        def isExit(x, y) -> bool:
            return x == 0 or x == m - 1 or y == 0 or y == n - 1
        
        m = len(maze)
        n = len(maze[0])
        directions = ((0, 1), (0, -1), (-1, 0), (1, 0))

        # label start as visited location
        maze[entrance[0]][entrance[1]] = "v"

        queue = deque([(entrance[0], entrance[1], 0)])

        while queue:
            x, y, steps = queue.popleft()

            if isExit(x, y) and steps != 0:
                return steps
            
            for dx, dy in directions:
                newX, newY, newS = x + dx, y + dy, steps + 1
                if valid(newX, newY):
                    maze[newX][newY] = "v"
                    queue.append((newX, newY, steps + 1))

        return -1



sol = Solution() 
