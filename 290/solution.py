class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''words = s.split(" ")
        
        if len(pattern) != len(words):
            return False

        matches = {}
        seen = set()
        for i in range(len(pattern)):
            p = pattern[i]
            if p not in matches and words[i] not in seen:
                matches[p] = words[i]
                seen.add(words[i])
            elif p not in matches or matches[p] != words[i]:
                return False

        return True'''

        # cleaned up solution, remove set requirement
        words = s.split(" ")
        
        if len(pattern) != len(words):
            return False

        matches = {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if p in matches:
                if matches[p] != w:
                    return False
            elif w in matches.values():
                return False
            else:
                matches[p] = w

        return True

sol = Solution() 
print(sol.wordPattern("abba", "d c c d"))
print(sol.wordPattern("abba", "d c c f"))
print(sol.wordPattern("aaaa", "d c c d"))
print(sol.wordPattern("abbacde", "d c c d e f g"))
print(sol.wordPattern("abc", "d c c"))
print(sol.wordPattern("aba", "d c c"))
print(sol.wordPattern("a", "d c"))
print(sol.wordPattern("aba", "d c"))
