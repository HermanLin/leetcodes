from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(curr, i):
            if i == N:
                if curr:
                    ans.append("".join(curr))
                return
            
            letters = phone[digits[i]]
            for l in letters:
                curr.append(l)
                dfs(curr, i + 1)
                curr.pop()
        
        
        phone = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz"
        }
        
        N = len(digits)
        ans = []
        dfs([], 0)
        return ans

sol = Solution() 
print(sol.letterCombinations("23"))
print(sol.letterCombinations("2"))
print(sol.letterCombinations(""))
print(sol.letterCombinations("7345"))
