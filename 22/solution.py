from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr, nOpen, nClose):
            if nOpen == n and nClose == n:
                ans.append("".join(curr))
                return
            
            if nOpen < n:
                curr.append("(")
                backtrack(curr, nOpen + 1, nClose)
                curr.pop()
                
            if nClose < nOpen:
                curr.append(")")
                backtrack(curr, nOpen, nClose + 1)
                curr.pop()
            
        ans = []
        backtrack(["("], 1, 0)
        return ans

sol = Solution() 
print(sol.generateParenthesis(1))
print(sol.generateParenthesis(2))
print(sol.generateParenthesis(3))
print(sol.generateParenthesis(4))
