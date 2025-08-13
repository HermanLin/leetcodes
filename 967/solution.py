from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        def backtrack(curr, prevDigit, nextPlace):
            if nextPlace < 0:
                ans.append(curr)
                return
            
            '''# subtract for next digit
            if prevDigit - k >= 0:
                next_digit = prevDigit - k
                increment = next_digit * (10 ** nextPlace)
                
                curr += increment
                backtrack(curr, next_digit, nextPlace - 1)
                curr -= increment
                
            # add for next digit
            if prevDigit + k <= 9:
                next_digit = prevDigit + k
                increment = next_digit * (10 ** nextPlace)
                
                curr += increment
                backtrack(curr, next_digit, nextPlace - 1)
                curr -= increment'''

            # refactored above code
            for op in operations:
                next_digit = prevDigit + (k * op)
                
                if 0 <= next_digit <= 9:
                    increment = next_digit * (10 ** nextPlace)
                    
                    curr += increment
                    backtrack(curr, next_digit, nextPlace - 1)
                    curr -= increment

        operations = [-1,1]
        if k == 0:
            operations.pop()
            
        ans = []
        for i in range(1, 10):
            backtrack(i * (10 ** (n - 1)), i, n - 2)
            
        return ans
    
    # another solution, simpler approach
    def numsSameConsecDiff2(self, n: int, k: int) -> List[int]:
        def backtrack(curr, left):
            if left == 0:
                ans.append(curr)
                return
            
            prev_digit = curr % 10

            if prev_digit - k >= 0:
                backtrack((curr * 10) + prev_digit - k, left - 1)

            if prev_digit + k <= 9 and k != 0:
                backtrack((curr * 10) + prev_digit + k, left - 1)

        ans = []
        for i in range(1, 10):
            backtrack(i, n - 1)

        return ans

sol = Solution() 
print(sol.numsSameConsecDiff(3, 7))
print(sol.numsSameConsecDiff(2, 1))
print(sol.numsSameConsecDiff(2, 0))
