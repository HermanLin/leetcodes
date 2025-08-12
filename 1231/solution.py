from typing import List


class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        '''N = len(sweetness)
        
        if N == k + 1:
            return min(sweetness)
        
        if k == 0:
            return sum(sweetness)
        
        def check(level):
            count = 0
            chunk_sweetness = 0
            
            for i in range(N):
                chunk_sweetness += sweetness[i]
                
                if chunk_sweetness >= level:
                    count += 1
                    chunk_sweetness = 0
            
            return count >= k + 1
        
        left = min(sweetness) # minimum = you get a chunk with the smallest sweetness
        right = sum(sweetness) # maximum = you get the entire chocolate bar
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(mid): # check if the minimum sweetness level works
                left = mid + 1
            else:
                right = mid - 1
                
        return right'''

        # improved solution, reduce complexities
        def check(level):
            count = 0
            chunk_sweetness = 0
            
            for piece in sweetness:
                chunk_sweetness += piece
                
                if chunk_sweetness >= level:
                    count += 1
                    chunk_sweetness = 0
            
            return count >= k + 1
        
        left = min(sweetness) # minimum = you get a chunk with the smallest sweetness
        right = sum(sweetness) // (k + 1) # maximum = you get the largest chunk between your friends 
        
        while left <= right:
            mid = (left + right) // 2
            
            if check(mid): # check if the minimum sweetness level works
                left = mid + 1
            else:
                right = mid - 1
                
        return right

sol = Solution() 
