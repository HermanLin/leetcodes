class Solution:
    def makeGood(self, s: str) -> str:
        '''great_stack = []

        for c in s:
            # if c is lower and gs[-1] is upper, remove
            if great_stack and ord(c) == (ord(great_stack[-1]) - 32):
                great_stack.pop()
            # if c is upper and gs[-1] is lower, remove
            elif great_stack and ord(c) == (ord(great_stack[-1]) + 32):
                great_stack.pop()
            else:
                great_stack.append(c)

        return "".join(great_stack)'''

        great_stack = []
        
        for c in s:
            if great_stack and c != great_stack[-1] and c.lower() == great_stack[-1].lower():
                great_stack.pop()
            else:
                great_stack.append(c)

        return "".join(great_stack)
    
sol = Solution()
print(sol.makeGood("leEeetcode"))
print(sol.makeGood("lEetcode"))
print(sol.makeGood("abBAcC"))