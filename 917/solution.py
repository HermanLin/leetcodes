from collections import deque


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        def isLetter(c):
            return "A" <= c <= "Z" or "a" <= c <= "z"
        '''
        N = len(s)
        ans = [""] * N

        left = 0
        right = N - 1

        while left <= right:
            if isLetter(s[left]) and isLetter(s[right]):
                ans[left] = s[right]
                ans[right] = s[left]
                left += 1
                right -= 1
            elif isLetter(s[left]):
                # right is guaranteed not a letter
                ans[right] = s[right]
                right -= 1
            else:
                ans[left] = s[left] 
                left += 1

        return "".join(ans)
        '''    

        # alternative approach
        N = len(s)
        ans = []

        letters = []
        symbols = deque([])

        for c in s:
            if isLetter(c):
                letters.append(c)
            else:
                symbols.append(c)

        for c in s:
            if isLetter(c):
                ans.append(letters.pop())
            else:
                ans.append(symbols.popleft())

        return "".join(ans)
        

sol = Solution() 
print(sol.reverseOnlyLetters("ab-cd"))
print(sol.reverseOnlyLetters("a-bC-dEf-ghIj"))
print(sol.reverseOnlyLetters("Test1ng-Leet=code-Q!"))
print(sol.reverseOnlyLetters("fgdngfhjh.,hd=--+-9989843kj%$3gfdfsh"))
print(sol.reverseOnlyLetters("arwegrehfdgfdgsd%$#dsffsdfhfd%$fgags-sdsdg=sdgsg===sgdsdgsd-dgdsgf-ghsdgdsggsgdIj"))
