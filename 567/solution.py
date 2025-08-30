class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            # s1 cannot be a permutation of s2
            return False
        
        def cToN(c):
            return ord(c) - 97
        
        # count s1 characters for comparison
        counts = [0] * 26
        for i in range(len(s1)):
            counts[cToN(s1[i])] += 1

        perm_counts = [0] * 26
        # sliding window to track permutation
        left = 0
        for right in range(len(s2)):
            i = cToN(s2[right])

            # increase window
            perm_counts[i] += 1

            if perm_counts == counts:
                return True

            # decrease window while permutation does not work
            while perm_counts[i] > counts[i]:
                perm_counts[cToN(s2[left])] -= 1
                left += 1

        return False

sol = Solution() 
