from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # "balloon" consists of:
        # 1 b, 1 a, 2 l's, 2 o's, 1 n
        # any time we have all of these letters, we increment our count
        '''balloon = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}

        for c in text:
            match c:
                case 'b' | 'a' | 'l' | 'o' | 'n':
                    balloon[c] += 1'''
        
        balloon = Counter(text)

        return min(
            balloon['b'], 
            balloon['a'], 
            balloon['n'], 
            balloon['l'] // 2, 
            balloon['o'] // 2
        )

sol = Solution()
print(sol.maxNumberOfBalloons("nlaebolko"))
print(sol.maxNumberOfBalloons("loonbalxballpoon"))
print(sol.maxNumberOfBalloons("leetcode"))
print(sol.maxNumberOfBalloons("balon"))
