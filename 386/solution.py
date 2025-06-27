from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        '''
        ans = []
        def generate(curr: int):
            # if the current larger than n, does not pass
            if curr > n:
                return
            
            ans.append(curr)
    
            # go up to the next lexicographically larger number
            # 1 -> 10 -> 100 -> ..., 2 -> 20 -> 200 -> ..., 3 -> ...
            for i in range(0, 10):
                generate(curr * 10 + i)

        # the start for each "set" of lexicographical numbers will be
        # a single digit 1..9
        for i in range(1, 10):
            generate(i)

        return ans
        '''
        
        # faster solution, true O(n) since we don't unnecessarily handle 
        # additional numbers from the last for loop in previous solution.
        # this could be O(1) extra space if you printed instead of storing
        # the answer in a list of O(n) space.
        ans = []
        curr = 1

        for _ in range(n):
            ans.append(curr)

            if curr * 10 <= n:
                curr = curr * 10
            else:
                # reset back to the next lexicographic set of numbers
                # when we're done adding the current batch 1 -> 10 -> 100...
                # e.g. 18 -> 19, curr % 10 == 9, curr = 1 -> curr = 2
                while curr % 10 == 9 or curr >= n:
                    curr = curr // 10
                
                curr += 1
        
        return ans


sol = Solution()
print(sol.lexicalOrder(13))
print(sol.lexicalOrder(2))
print(sol.lexicalOrder(23))
print(sol.lexicalOrder(100))
