from typing import List


class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        N = len(arr)
        visited = set()
        stack = [start]
        
        while stack:
            index = stack.pop()
            
            if arr[index] == 0:
                return True
            
            if index in visited:
                continue

            visited.add(index)
            
            plus, minus = index + arr[index], index - arr[index]
            
            if plus not in visited and plus < N:
                # visited.add(plus)
                stack.append(plus)
            if minus not in visited and minus > -1:
                # visited.add(minus)
                stack.append(minus)
                
        return False

sol = Solution() 
