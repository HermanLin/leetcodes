from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # mag_dict = defaultdict(int)
        # for letter in magazine:
        #     mag_dict[letter] += 1
        
        mag_dict = Counter(magazine)

        for letter in ransomNote:
            if mag_dict[letter]:
                mag_dict[letter] -= 1
            else:
                return False

        return True
        

        '''
        # another solution, using array instead of map
        mag = [0] * 26 # 26 lowercase letters

        for letter in magazine:
            mag[ord(letter) - ord("a")] += 1
        
        for letter in ransomNote:
            key = ord(letter) - ord("a")
            if mag[key]:
                mag[key] -= 1
            else:
                return False
            
        return True
        '''

    
sol = Solution()
print(sol.canConstruct("a","b"))
print(sol.canConstruct("aa","ab"))
print(sol.canConstruct("aa","aab"))
print(sol.canConstruct("fihjjjjei","hjibagacbhadfaefdjaeaebgi"))
