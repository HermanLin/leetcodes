import string
import pdb

# bababcaba
'''
p           s           t
            bababcaba   
            babcaba     ba
a           babcaba     b
a           bcaba       bba
aa          bcaba       bb
aa          ba          bbbca
aaa         ba          bbbc
aaa                     bbbcba
aaaabcbbb
'''

# bzeyxf
'''
p       s       t
        zeyxf   b
b       zeyxf   
b       eyxf    z
b       yxf     ze
be      yxf     z
be      xf      zy
be      f       zyx
be              zyxf
befxyz        
'''

class Solution:
    def robotWithString(self, s: str) -> str:
        N = len(s)

        # each element represents the smallest character
        # in the substring from s[i] to s[N- 1]
        smallest_after = [''] * N
        
        # go from right to left
        smallest_after[N-1] = s[-1]
        for i in range(N-2, -1, -1):
            smallest_after[i] = min(smallest_after[i+1], s[i])

        # now we can determine in O(1) whether or not
        # there still exists a char smaller than the current i

        t = []
        p = []
        for i in range(N):
            # if there are chars to pop and the top element
            # is the smallest of its substring...
            while len(t) > 0 and t[-1] <= smallest_after[i]:
                p.append(t.pop())

            # if the stack is empty or the top element
            # is not the smallest of its substring
            if not t or t[-1] > smallest_after[i]:
                t.append(s[i])
                
        # the rest of `p` is just t reversed
        while t:
            p.append(t.pop())

        return ''.join(p)
    
sol = Solution()
print(sol.robotWithString('zza'))
print(sol.robotWithString('bac'))
print(sol.robotWithString('bdda'))
print(sol.robotWithString('bababcaba'))
print(sol.robotWithString('bzeyxf'))

