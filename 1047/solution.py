class Solution:
    def removeDuplicates(self, s: str) -> str:
        removal_stack = []

        for c in s:
            if removal_stack and c == removal_stack[-1]:
                removal_stack.pop()
            else:
                removal_stack.append(c)

        return ''.join(removal_stack)
    
sol = Solution()
print(sol.removeDuplicates("abbaca"))
print(sol.removeDuplicates("azxxzy"))
print(sol.removeDuplicates("jguufstqgbhbgwycabakuiyymhgtlool"))
print(sol.removeDuplicates("fgpbgcwanrporqzgefpbsrqlodbqzxnj"))
print(sol.removeDuplicates("qhnlxqnqvngyvqxeionxdheaymubtseo"))
