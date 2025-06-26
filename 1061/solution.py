import collections
import string

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        '''
        N = len(s1)
        equiv_map = {}
        for i in range(N):
            if s1[i] not in equiv_map and s2[i] in equiv_map:
                equiv_map[s1[i]] = equiv_map[s2[i]]
            elif s2[i] not in equiv_map and s1[i] in equiv_map:
                equiv_map[s2[i]] = equiv_map[s1[i]]
            else:
                equiv_map[s1[i]] = equiv_map[s2[i]] = i
        '''

        '''
        N = len(s1)
        # initialize and equivalence map, where each letter maps to itself.
        # this will be used to represent the lexico. smallest with each union of chars.
        equiv_map = {}
        for c in range(97, 123): # <- string.ascii_lowercase to loop through lowercase letters
            equiv_map[chr(c)] = chr(c)

        # loop through each string and evaluate the chars' unions.
        for i in range(N):
            eq_s1 = equiv_map[s1[i]]
            eq_s2 = equiv_map[s2[i]]

            if eq_s1 < eq_s2:
                cmp = s2[i]
                # need to backtrack when possible to set each previous
                # char's lexico. smallest to the new smallest.
                while cmp != eq_s1:
                    temp = equiv_map[cmp]
                    equiv_map[cmp] = eq_s1
                    cmp = temp

            elif eq_s2 < eq_s1:
                cmp = s1[i]
                while cmp != eq_s2:
                    temp = equiv_map[cmp]
                    equiv_map[cmp] = eq_s2
                    cmp = temp

        lexico_smallest = ''
        for c in baseStr:
            # catch any leftover backtracks we couldn't handle before
            # due to a char being processed after a new lexico. smallest
            # has been added.
            prev_root = c
            root = equiv_map[c]
            while prev_root != root:
                prev_root = root
                root = equiv_map[root]

            lexico_smallest += root

        return lexico_smallest
        '''

        # construct an adjacency list for each character between the words
        adj_list = collections.defaultdict(list)
        for c1, c2 in zip(s1, s2):
            adj_list[c1].append(c2)
            adj_list[c2].append(c1)

        print(adj_list)

        smallest = {}
        for c in string.ascii_lowercase:
            if c not in smallest:
                q = collections.deque()
                smallest[c] = c
                q.append(c)

                while len(q) > 0:
                    curr = q.popleft()

                    # evaluate all nodes reachable from `c` to equal `c`
                    for v in adj_list[curr]:
                        if v not in smallest:
                            smallest[v] = c
                            q.append(v)

        print(smallest)

        lexico_smallest = ''
        for c in baseStr:
            lexico_smallest += smallest[c]

        return lexico_smallest

sol = Solution()
# print(sol.smallestEquivalentString('parker','morris','parser'))
# print(sol.smallestEquivalentString('hello','world','hold'))
print(sol.smallestEquivalentString('leetcode','programs','sourcecode'))
# leetcode
# programs
# print(sol.smallestEquivalentString('adkbbjigibahbjjgdkkiighagijfdfjkcdaakdkbjcidgjjfga','hbfahdikgchbkigebgjghdhadaikhccjejafkaibdgffichcbb','hotutsrhanyvpzusrnsxbncpqhnxrvgmbrpcbhheqotadyzfyl'))
