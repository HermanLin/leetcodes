from typing import List
from collections import defaultdict

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # track how many times a particular order appears...
        order_count = defaultdict(int)
        for row in grid:
            order_count[tuple(row)] += 1

        # ...then generate column orders and compare
        count = 0
        N = len(grid)
        for i in range(N):
            col_order = []
            for j in range(N):
                col_order.append(grid[j][i])

            count += order_count[tuple(col_order)]

        return count
    
sol = Solution()
print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
print(sol.equalPairs([[3,2,1],[1,7,6],[2,7,7]]))
print(sol.equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))
print(sol.equalPairs([[13,13],[13,13]]))
print(sol.equalPairs([[2,1],[3,32]]))
print(sol.equalPairs([[3,1,2,2],[1,4,4,4],[2,4,2,2],[2,5,2,2]]))
print(sol.equalPairs([[1,1,14103,51308],[1,2,1,1],[1,1,1,1],[1,1,1,1]]))
print(sol.equalPairs([[2,22],[22,2]]))