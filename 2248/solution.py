from typing import List
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        counts = defaultdict(int)

        for sub_nums in nums:
            for num in sub_nums:
                '''
                if num not in counts:
                    counts[num] = 0
                counts[num] += 1
                '''
                # defaultdict initializes as 0 if not present
                counts[num] += 1

        ans = []
        N = len(nums)
        '''
        for k, v in counts.items():
            if v == N:
                ans.append(k)
        '''
        # just as simple to loop by key and access the value
        for k in counts:
            if counts[k] == N:
                ans.append(k)

        return sorted(ans)
    
sol = Solution()
print(sol.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(sol.intersection([[3,1,2,4,5],[1,2,3,4],[4,3,5,6]]))
print(sol.intersection([[1,2,3],[4,5,6]]))
