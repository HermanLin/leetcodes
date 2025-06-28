class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        # below solution too slow for largest constraint.
        # takes time to generate the kth number
        '''
        curr = 1

        for _ in range(k):
            if k == 1: 
                break
            
            k -= 1
            if curr * 10 <= n:
                curr = curr * 10
            else:
                # reset back to the next lexicographic set of numbers
                # e.g. 18 -> 19, curr % 10 == 9, curr = 1 -> curr = 2
                while curr % 10 == 9 or curr >= n:
                    curr = curr // 10
                
                curr += 1

        return curr
        '''


        '''
        n = 1
        -> 1
        number under each prefix:
        [1]

        n = 10
        -> 1, 10, 2, 3, 4, 5, 6, 7, 8, 9
        number under each prefix:
        [2, 1, 1, 1, 1, 1, 1, 1, 1]
        
        n = 20
        -> 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9
        number under each prefix:
        [11, 2, 1, 1, 1, 1, 1, 1, 1]

        n = 13
        -> 1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9
        number under each prefix:
        [5, 1, 1, 1, 1, 1, 1, 1, 1]
        '''

        curr = 1

        for _ in range(k):
            if k == 1: 
                break
            
            k -= 1
            if curr * 10 <= n:
                curr = curr * 10
            else:
                # reset back to the next lexicographic set of numbers
                # e.g. 18 -> 19, curr % 10 == 9, curr = 1 -> curr = 2
                while curr % 10 == 9 or curr >= n:
                    curr = curr // 10
                
                curr += 1

        return curr
    

    
sol = Solution()

print(sol.findKthNumber(13, 2))
print(sol.findKthNumber(1, 1))
print(sol.findKthNumber(13, 1))
print(sol.findKthNumber(100, 10))
print(sol.findKthNumber(1000000000,1000000000))
