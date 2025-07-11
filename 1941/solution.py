class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        counts = {}

        for c in s:
            if c in counts:
                counts[c] += 1
            else:
                counts[c] = 1

        
        frequency = counts[s[0]]
        for k in counts:
            if counts[k] != frequency:
                return False

        return True
        
        '''return len(set(counts.values())) == 1'''
    
sol = Solution()
print(sol.areOccurrencesEqual('abacbc'))
print(sol.areOccurrencesEqual('aaabb'))
print(sol.areOccurrencesEqual('bbaaa'))
print(sol.areOccurrencesEqual('qwertyuiopasdfghjklzxcvbnm'))
