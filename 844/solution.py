class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''def cleanString(s: str) -> str:
            stack = []
            for c in s:
                # if stack and c == "#":
                #     stack.pop()
                # elif c != "#":
                #     stack.append(c)

                if c != "#":
                    stack.append(c)
                elif stack:
                    stack.pop()
            return ''.join(stack)
        
        return cleanString(s) == cleanString(t)'''

        # alternative solution with O(1) space instead
        s_ptr = len(s) - 1
        t_ptr = len(t) - 1
        s_skips = t_skips = 0

        while s_ptr >= 0 or t_ptr >= 0:
            # if there are still characters to consider...
            while s_ptr >= 0:
                # if it's a backspace...
                if s[s_ptr] == "#":
                    # add to the skip counter and decrement
                    s_skips += 1
                    s_ptr -= 1
                # if it's [a-z] and there are letters to skip...
                elif s_skips:
                    # "skip" one and decrement
                    s_skips -= 1
                    s_ptr -= 1
                # we've reached a character to compare with
                else: 
                    break

            # same process as above
            while t_ptr >= 0:
                if t[t_ptr] == "#":
                    t_skips += 1
                    t_ptr -= 1
                elif t_skips:
                    t_skips -= 1
                    t_ptr -= 1
                else:
                    break

            # if we're at the beginning of both strings...
            if s_ptr < 0 and t_ptr < 0:
                return True
            # if we're only at the beginning of one string...
            elif s_ptr < 0 or t_ptr < 0:
                return False
            # if the chars we're comparing do not match...
            elif s[s_ptr] != t[t_ptr]:
                return False
            
            # on to the next character
            s_ptr -= 1
            t_ptr -= 1

        return True
    
sol = Solution()
print(sol.backspaceCompare("ab#c", "ad#c"))
print(sol.backspaceCompare("ab##", "c#d#"))
print(sol.backspaceCompare("a#c", "b"))
print(sol.backspaceCompare("#", "b#"))


# def countBackspaces(s: str) -> int:
#             count = 0
#             for c in s: 
#                 count += 1 if c == "#" else 0
#             return count

#         print(countBackspaces(s))
#         print(countBackspaces(t))
