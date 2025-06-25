class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word

        N = len(word)
        largest_substr = ''

        # the largest a substring can be is: N - numFriends + 1
        # this guarantees all other friends has a len(substr) of 1
        longest = N - numFriends + 1
        
        # for length in range(0, longest):
        #     for beginning in range(length, N - length):
        #         end = beginning + length
        #         substr = word[beginning:end]

        #         # if isLexicographicallyLarger(substr, largest_substr):
        #         #     largest_substr = substr

        #         if substr > largest_substr:
        #             largest_substr = substr

        for i in range(N):
            beginning = i
            end = i + longest
            substr = word[beginning:end]

            if substr > largest_substr:
                largest_substr = substr

        return largest_substr

        # Alternative solution to achieve O(nlogn)
        # use a suffix array and reconstruct the lexico. largest string

    
# returns True if a is lexicographically larger than b, else False
def isLexicographicallyLarger(a: str, b: str) -> bool:
    idx = 0
    
    while idx < len(a) and idx < len(b):
        if a[idx] < b[idx]:
            return False
        
        if a[idx] > b[idx]:
            return True
        
        idx += 1

    if len(a) < len(b):
        return False
    
    return True