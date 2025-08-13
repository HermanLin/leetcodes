from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        '''def backtrack(curr, path, i):
            if curr == n and len(path) == k:
                ans.append(path[:])
                return
            
            if curr < n:
                for j in range(i, 10):
                    if curr + j <= n:
                        path.append(j)
                        backtrack(curr + j, path, j + 1)
                        path.pop()
        
        ans = []
        for i in range(1, 10):
            backtrack(i, [i], i+1)
            
        return ans'''

        # alternative solution
        def backtrack(curr, path, i, left):
            if curr == n and left == 0:
                ans.append(path[:])
                return
            
            if curr > n or left == 0:
                return
            
            for j in range(i, 10):
                backtrack(curr + j, path + [j], j + 1, left - 1)

        ans = []
        backtrack(0, [], 1, k)
        return ans

sol = Solution() 
print(sol.combinationSum3(3, 7))
print(sol.combinationSum3(3, 9))
print(sol.combinationSum3(4, 1))
