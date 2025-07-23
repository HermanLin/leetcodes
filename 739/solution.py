from typing import List

class Solution: 
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        
        # use monotonic stack to store indicies of temps
        # whenever we encounter a lower temp, push
        # whenever we encounter a higher temp, pop till it's lower
        m_stack = []
        ans = [0] * N

        for i in range(N):
            while m_stack and temperatures[m_stack[-1]] < temperatures[i]:
                j = m_stack.pop()

                # set to index of +temp minus index of -temp
                ans[j] = i - j

            m_stack.append(i)

        return ans

sol = Solution() 
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
print(sol.dailyTemperatures([30,40,50,60]))
print(sol.dailyTemperatures([30,60,90]))