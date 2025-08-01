from collections import defaultdict, deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''n = len(beginWord)
        valid = set(wordList)
        
        if endWord not in valid:
            return 0
        
        seen = set([beginWord])
        queue = deque([(beginWord, 1)])
        
        while queue:
            word, seq_count = queue.popleft()
            
            if word == endWord:
                return seq_count
            
            for c in "abcdefghijklmnopqrstuvwxyz":
                for i in range(n):
                    transformed = word[:i] + c + word[i+1:]
                    if transformed in valid and transformed not in seen:
                        seen.add(transformed)
                        queue.append((transformed, seq_count + 1))
                        
        return 0'''

        # improved solution, use pattern heuristics to reduce
        # the number of words we are searching against
        if endWord not in wordList:
            return 0
        
        n = len(beginWord)
        patterns = defaultdict(list)
        
        # pre-process wordList into mapping of matching patterns
        for word in wordList:
            for i in range(n):
                pattern = word[:i] + "*" + word[i+1:]
                patterns[pattern].append(word)

        seen = {beginWord}
        queue = deque([(beginWord, 1)])

        while queue:
            word, seq_count = queue.popleft()

            for i in range(n):
                pattern = word[:i] + "*" + word[i+1:]

                if patterns[pattern]:
                    for p in patterns[pattern]:
                        if p == endWord:
                            return seq_count + 1
                        if p not in seen:
                            seen.add(p)
                            queue.append((p, seq_count + 1))
                    
                    # done working with this pattern,  
                    # let's remove it from consideration
                    del patterns[pattern]

        return 0


sol = Solution() 
# 5
print(sol.ladderLength("hit","cog",["hot","dot","dog","lot","log","cog"]))
# 0
print(sol.ladderLength("hit","cog",["hot","dot","dog","lot","log"]))
# 6
print(sol.ladderLength("leet","code",["lest","leet","lose","code","lode","robe","lost"]))
# 4
print(sol.ladderLength("hbo","qbx",["abo","hco","hbw","ado","abq","hcd","hcj","hww","qbq","qby","qbz","qbx","qbw"]))
# 2
print(sol.ladderLength("a","c",["a","b","c"]))
# 5
print(sol.ladderLength("qa","sq",["si","go","se","cm","so","ph","mt","db","mb","sb","kr","ln","tm","le","av","sm","ar","ci","ca","br","ti","ba","to","ra","fa","yo","ow","sn","ya","cr","po","fe","ho","ma","re","or","rn","au","ur","rh","sr","tc","lt","lo","as","fr","nb","yb","if","pb","ge","th","pm","rb","sh","co","ga","li","ha","hz","no","bi","di","hi","qa","pi","os","uh","wm","an","me","mo","na","la","st","er","sc","ne","mn","mi","am","ex","pt","io","be","fm","ta","tb","ni","mr","pa","he","lr","sq","ye"]))
