class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        tracker = set()
        left = longest = 0

        N = len(s)
        for right in range(N):
            if s[right] not in tracker:
                tracker.add(s[right])
            else:
                while left < right:
                    if s[left] == s[right]:
                        left += 1
                        break
                    else:
                        tracker.remove(s[left])
                        left += 1
            
            longest = max(longest, right - left + 1)
                          
        return longest
        '''

        # improve functionality
        tracker = set()
        left = longest = 0

        N = len(s)
        for right in range(N):
            while s[right] in tracker:
                tracker.remove(s[left])
                left += 1
            
            tracker.add(s[right])
            longest = max(longest, right - left + 1)

        return longest


    
sol = Solution()
print(sol.lengthOfLongestSubstring("abcabcbb"))
print(sol.lengthOfLongestSubstring("bbbbb"))
print(sol.lengthOfLongestSubstring("pwwkew"))
print(sol.lengthOfLongestSubstring(" "))
print(sol.lengthOfLongestSubstring("dvd))f"))
print(sol.lengthOfLongestSubstring("cki))lbkd"))
print(sol.lengthOfLongestSubstring("tmmzuxt"))
print(sol.lengthOfLongestSubstring("jbpnbwwd"))
print(sol.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#%&()+,-.:;<=>?@[]^_{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-.:;<=>?@[]^_{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#%&()+,-.:;<=>?@[]^{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-.:;<=>?@[]^_{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#%&()*+,-./:;<=>?@[]^{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&()*+,-.:;<=>?@[]^_{|}~ abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!"))