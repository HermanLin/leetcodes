from typing import List

class Solution:
    def countElements(self, arr: List[int]) -> int:
        # naive approach, O(n^2) time
        '''
        count = 0
        for x in arr:
            for y in arr:
                if x == y + 1:
                    count += 1

        return count
        '''

        # improved approach, O(n) time w/ O(n) space
        unique_elems = set(arr)
        count = 0

        for num in arr:
            if num + 1 in unique_elems:
                count += 1

        return count

sol = Solution()
print(sol.countElements([1,2,3]))
print(sol.countElements([1,1,3,3,5,5,7,7]))
