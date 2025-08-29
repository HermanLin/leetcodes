from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        '''n = len(pushed)
        m = len(popped)
        ptr1 = ptr2 = 0

        stack = []
        
        while ptr1 < n or ptr2 < m:
            print(stack, ptr1, ptr2)

            if stack and popped[ptr2] == stack[-1]:
                stack.pop()
                ptr2 += 1
            else:
                if ptr1 == n:
                    return False
                    
                stack.append(pushed[ptr1])
                ptr1 += 1

        return True'''

        stack = []
        ptr = 0

        for i in range(len(pushed)):
            stack.append(pushed[i])
            while stack and stack[-1] == popped[ptr]:
                stack.pop()
                ptr += 1

        if stack:
            return False
        return True
            
        

sol = Solution() 
