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

        n = 13
        -> 1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9
        number under each prefix:
        [5, 1, 1, 1, 1, 1, 1, 1, 1]
        
        n = 20
        -> 1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9
        number under each prefix:
        [11, 2, 1, 1, 1, 1, 1, 1, 1]       


        we want to generate some kind of "prefix trie"
        where the number 1 has children 10, 11, 12, ..., up to 19. 
        similarly, 2 has children 20, 21, ..., up to 29 and so on for other numbers.
        '''

        # count how many numbers exist between two prefixes
        # e.g. for n = 20, how many numbers exist between 1 and 2 (1 inclusive) -> 11
        def countSteps(prefix1: int, prefix2: int) -> int:
            steps = 0

            while prefix1 <= n:
                # cap prefix2 at `n + 1` in case prefix2 > n
                steps += min(n + 1, prefix2) - prefix1

                # traverse deeper down the prefix trie
                prefix1 *= 10
                prefix2 *= 10

            return steps

        curr = 1
        k -= 1 # 'curr' being `1` means we've considered one number already; edge case

        while k > 0:
            steps = countSteps(curr, curr + 1)

            # if steps are <= k...
            if steps <= k:
                # ...skip this prefix's subtree
                # move to the next prefix and decrease k by how many numbers we skipped
                curr += 1
                k -= steps
            else:
                # ...move to the next level of the tree and decrement k by 1
                # decrease k by 1 since we've stepped to the next lexicographical number
                curr *= 10
                k -= 1

        return curr


sol = Solution()

print(sol.findKthNumber(13, 2))
print(sol.findKthNumber(1, 1))
print(sol.findKthNumber(20, 13))
print(sol.findKthNumber(100, 10))
print(sol.findKthNumber(1000000000,1000000000))
