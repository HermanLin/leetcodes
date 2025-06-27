import heapq

class Solution:
    '''
    additional examples:
    "aaba*"         => "aab"
    "abc"           => "abc"
    "abc*de*fgh*"   => "defgh"
    "a*b*c*d*"      => ""
    "abcde*f*"      => "cdef"
    "abc*"          => "bc"
    "aaaa***"       => "a"
    "caba*"         => "cab"
    '''
    def clearStars(self, s: str) -> str:
        # O(NlogN) solution
        '''
        N = len(s)

        # use a min heap to track the lexico. smallest letter and its index
        min_heap = []
        # keep track of indexes we've removed for later processing
        removed_indexes = set()
        for i in range(N):
            if s[i] == '*':
                c, idx = heapq.heappop(min_heap)
                # don't forget to re-invert the index to get its proper loc.
                removed_indexes.add(-idx)
            else:
                # we want to remove the right most letter that is left of a '*'.
                # invert the index to keep the min heap working as expected.
                # ('a', -5) < ('a',-20)
                # ('a', -5) < ('b',-20)
                heapq.heappush(min_heap, (s[i], -i))

        cleared = []
        for i in range(N):
            if s[i] != '*' and i not in removed_indexes:
                cleared.append(s[i])

        return ''.join(cleared)
        '''

        # O(Nlog(alpha)) solution
        # each stack of 'counts' represents each letter
        counts = [[] for _ in range(26)]
        arr = list(s)
        for i, c in enumerate(arr):
            if c != "*":
                # keep track of the location of the character's index
                counts[ord(c) - ord("a")].append(i)
            else:
                for j in range(26):
                    # if the smallest letter is available...
                    if counts[j]: 
                        # ...convert its letter to a star in the string
                        arr[counts[j].pop()] = "*" 
                        break

        # convert the array back into a string, skipping over stars
        return "".join(c for c in arr if c != "*")


sol = Solution()
print(sol.clearStars('aaba*'))
print(sol.clearStars('abc*de*fgh*'))
print(sol.clearStars('a*b*c*d*'))
print(sol.clearStars('abc'))
print(sol.clearStars('caba*'))
