class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        N = len(s)
        mapping = {}
        seen = set()

        for i in range(N):
            if s[i] not in mapping:
                if t[i] not in seen:
                    mapping[s[i]] = t[i]
                    seen.add(t[i])
                else:
                    return False
            elif mapping[s[i]] != t[i]:
                return False
        
        return True
        

sol = Solution() 
