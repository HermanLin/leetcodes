from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            # easily compare strings together after "sorting" them.
            # you can also use a tuple(26) representing the count of each
            # character in s. This would reduce the overall complexity by
            # removing the need to sort. However, this would be worse for
            # smaller strings. 
            key = "".join(sorted(s)) 
            anagrams[key].append(s)

        '''
        ans = []
        for k in anagrams:
            ans.append(anagrams[k])

        return ans
        '''
        return list(anagrams.values())
    
sol = Solution()
print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
print(sol.groupAnagrams([""]))
print(sol.groupAnagrams(["a"]))
print(sol.groupAnagrams(["a",""]))
print(sol.groupAnagrams(["dab","fla","hip","his","any","yep","mae","wed","sow","gum","ate","ate","yep","raw","pan","haw","geo","bud"]))
