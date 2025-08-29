from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        zero = end = len(nums) - 1

        while zero >= 0 and end >= 0:
            print(zero,end)
            if nums[zero] != 0:
                zero -= 1
            else:
                # bubble zero to the end
                bubble = zero
                while bubble < end:
                    nums[bubble], nums[bubble + 1] = nums[bubble + 1], nums[bubble]
                    bubble += 1

                end -= 1
        '''

        N = len(nums)
        zero = 0
        
        for i in range(N):
            if nums[i] != 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1


sol = Solution() 
