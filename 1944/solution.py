from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        '''N = len(heights)
        ans = [0] * N

        stack = []
        for i in range(N - 1, -1, -1):
            # print(i, stack, heights[i])
            if stack:
                if heights[i] < stack[-1]:
                    stack.append(heights[i])
                    ans[i] = 1
                else:
                    while stack and heights[i] > stack[-1]:
                        stack.pop()
                        ans[i] += 1
                    
                    if stack:
                        ans[i] += 1

                    stack.append(heights[i])
            else:
                stack.append(heights[i])

        return ans'''
        
        '''N = len(heights)
        ans = [0] * N

        stack = []
        for i in range(N - 1, -1, -1):
            if stack and heights[i] < stack[-1]:
                ans[i] = 1
            else:
                while stack and heights[i] > stack[-1]:
                    stack.pop()
                    ans[i] += 1
                
                if stack:
                    ans[i] += 1

            stack.append(heights[i])

        return ans'''

        # final refactoring below
        N = len(heights)
        ans = [0] * N

        stack = []
        for i in range(N - 1, -1, -1):
            while stack and heights[i] > stack[-1]:
                stack.pop()
                ans[i] += 1
            
            if stack:
                ans[i] += 1
            
            stack.append(heights[i])

        return ans

sol = Solution() 
print(sol.canSeePersonsCount([30050,62544,79048,2931,70590,40244,52614,20769,82267,94422,7815,12736,34681]))
print(sol.canSeePersonsCount([10,6,8,5,11,9]))
print(sol.canSeePersonsCount([5,1,2,3,10]))
print(sol.canSeePersonsCount([10,6,7,5,11,8,9]))
