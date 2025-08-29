from typing import List


class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        ptr1 = ptr2 = 0

        while ptr1 < n and ptr2 < m:
            a = nums1[ptr1]
            b = nums2[ptr2]

            if a == b:
                return nums1[ptr1]

            if a < b:
                ptr1 += 1
            else:
                ptr2 += 1
        
        return -1

sol = Solution() 
