class Solution:
    def isValid(self, s: str) -> bool:
        '''stack = []

        for c in s:
            match c:
                case "(" | "{" | "[":
                    stack.append(c)
                case ")":
                    if len(stack) and stack[-1] == "(": stack.pop()  
                    else: return False
                case "}":
                    if len(stack) and stack[-1] == "{": stack.pop()  
                    else: return False
                case "]":
                    if len(stack) and stack[-1] == "[": stack.pop()  
                    else: return False

        if len(stack):
            return False

        return True'''

        # improved solution, cleaner implementation
        pairing = { ")":"(", "}":"{", "]":"[" }
        stack = []

        for c in s:
            if c in pairing:
                if stack and stack[-1] == pairing[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return False if stack else True