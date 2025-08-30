from typing import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # for two words to be close, three properties must be true:
        # 1. both words are of the same length
        # 2. both words contain the same letters
        # 3. the letter frequencies match (not necessarily the letters themselves)

        if len(word1) != len(word2):
            return False

        counts1 = Counter(word1)
        counts2 = Counter(word2)

        # check presence
        for c in counts1:
            if c not in counts2:
                return False

        # check frequencies
        if sorted(counts1.values()) == sorted(counts2.values()):
            return True

        return False

sol = Solution() 
