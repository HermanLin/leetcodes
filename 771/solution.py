class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_ids = set(jewels)

        count = 0
        for s in stones:
            if s in jewel_ids:
                count += 1

        return count
    
sol = Solution()
print(sol.numJewelsInStones("aA","aAAbbbb"))
print(sol.numJewelsInStones("z","ZZ"))
