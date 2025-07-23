from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        '''N2 = len(nums2)
        
        next_greatest = {}
        stack = []
        # we want the next greatest to the right, so start from the end of nums2
        for i in range(N2-1, -1, -1):
            # remove anything from our monotonic stack that is less than our curr
            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                # anything present in the stack is guaranteed to be greater
                # than and to the right of our current number
                next_greatest[nums2[i]] = stack[-1]
            else:
                # ...otherwise, -1 because nothing is greater than and to the right
                next_greatest[nums2[i]] = -1

            # add the number to the stack for consideration for nums to the left.
            # this number will be the "next greatest" to the right 
            stack.append(nums2[i])

        ans = []
        for n in nums1:
            ans.append(next_greatest[n])

        return ans'''

        # improved solution, reduce complexity
        next_greatest = {}
        stack = []
        for n in nums2:
            # remove anything from our stack that is less than curr.
            # those removed are guaranteed to have curr as the next greatest
            while stack and stack[-1] < n:
                next_greatest[stack.pop()] = n
            
            stack.append(n)

        ans = []
        for n in nums1:
            ans.append(next_greatest.get(n, -1))

        return ans

 
sol = Solution() 
print(sol.nextGreaterElement([4,1,2],[1,3,4,2]))
print(sol.nextGreaterElement([2,4],[1,2,3,4]))