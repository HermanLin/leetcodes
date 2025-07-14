from typing import List

class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        unique = set()
        common = set()

        for num in nums:
            if num not in unique:
                if num not in common:
                    unique.add(num)
            else:
                unique.remove(num)
                common.add(num)

        largest = -1
        for n in unique:
            if n > largest:
                largest = n

        return largest
    
sol = Solution()
print(sol.largestUniqueNumber([5,7,3,9,4,9,8,3,1]))
print(sol.largestUniqueNumber([9,9,8,8]))
print(sol.largestUniqueNumber([669,669,434,434,615,615,133,133,849,849,372,372,101,101,203,203,209,209,380,380,712,712,362,362,84,84,401,401,664,664,362,362,663,663,128,128,131,131,851,851,344,344,88,88,120,120,179,179,791,791,300,300,901,901,980,980,622,622,873,873,194,194,600,600,42,42,923,923,645,645,572,572,216,216,123,123,47,47,687,687]))
