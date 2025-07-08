class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
    
sol = Solution()

print(sol.checkIfPangram("thelazydogthequickbrownfoxjumpsoverthelazydog"))
print(sol.checkIfPangram("leetcode"))
print(sol.checkIfPangram("abcdefghijklmnopqrstuvwxyz"))
print(sol.checkIfPangram("abcdefghijklmnopqrstuvwxy"))
