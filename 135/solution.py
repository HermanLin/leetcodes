from typing import List

# Example 1: [1,2,2,0,1,6,2,4,4,3]
# Answer 1: [1,2,2,1,2,3,1,2,2,1]
# Example 2: [1,2,3,4,5]
# Answer 2: [1,2,3,4,5]

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # -- Initial solution --
        # time complexity: O(n)
        # space complexity: O(n)
        '''
        minimum = 0
        distribution = [1] * len(ratings)

        # left pass
        for i in range(1, len(ratings)):
            # [A, B, C]
            # A < B, B must have at least 1 more than A
            if ratings[i] > ratings[i-1]:    
                distribution[i] = distribution[i-1] + 1

        # Example 1 after left pass: [1,2,1,1,2,3,1,2,2,1]
        # Example 2 after left pass: [1,2,3,4,5]

        # right pass
        for i in range(len(ratings) - 1, 0, -1):
            # [A, B, C]
            # B > C, B must have at least more candies than C
            if ratings[i-1] > ratings[i]:
                distribution[i-1] = max(distribution[i] + 1, distribution[i-1])
                
            # count as we go backwards, we've set the distribution for [i-1] in stone
            minimum += distribution[i-1] 

        # Example 1 after right pass: [1,2,2,1,2,3,1,2,2,1]
        # Example 2 after right pass: [1,2,3,4,5]

        # add the last distribution
        minimum += distribution[len(ratings) - 1]

        return minimum
        '''
    
        # -- Improved Solution --
        # time complexity: O(n)
        # space complexity: O(1)
        n = len(ratings)
        total = n # each child must have at least 1 candy
        i = 1 # start from second child

        while i < n:
            # if B == A, don't need to add any candies
            if ratings[i] == ratings[i-1]:
                i += 1
                continue

            # tracking increasing slope
            # B > A, add a candy to the total
            curr_peak = 0
            while i < n and ratings[i] > ratings[i-1]:
                curr_peak += 1
                total += curr_peak
                i += 1

            if i == n:
                return total
            
            # tracking decreasing slope
            # B < A, add a candy to the total, A should have >= than B
            curr_valley = 0
            while i < n and ratings[i] < ratings[i-1]:
                curr_valley += 1
                total += curr_valley
                i += 1

            # we double counted our peak when tracking both increasing/decreasing slope
            # we only care about the higher of the "two peaks"
            total -= min(curr_peak, curr_valley)

        return total