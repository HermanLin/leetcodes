class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # -- naive approach --
        # each child can have at most 'limit' candies, 
        # find out how many permutations sum up to 'n' candies.
        # min(n + 1, limit + 1) because a child can get 0 to n candies, limit can also be greater than n
        '''
        count = 0
        for i in range(min(n + 1, limit + 1)):
            for j in range(min(n + 1, limit + 1)):
                for k in range(min(n + 1, limit + 1)):
                    if i + j + k == n:
                        count += 1
        return count
        '''


        # -- improved naive approach --
        # you don't need to know about the third child, 
        # they get what's leftover
        '''
        count = 0
        for i in range(min(n + 1, limit + 1)):
            for j in range(min(n + 1, limit + 1)):
                k = n - i - j
                if k <= limit and k >= 0:
                    count += 1
        return count
        '''


        # -- ideal approach --
        # how many ways to distribute n - i candies, with a limit
        '''
        count = 0
        for i in range(min(n + 1, limit + 1)):
            candies_left = n - i
            # j                 k
            # 0             candies_left
            # 1             candies_left - 1
            # 2             candies_left - 2
            # 3             candies_left - 3
            # 4             candies_left - 4
            # ...
            # limit         candies_left - limit
            # ...
            # candies_left  0
            if limit >= candies_left:
                count += candies_left + 1
            else:
                # 5, 3 -> 2 ways
                # 5, 2 -> 0 ways
                # 6, 3 -> 1 way
                # 6, 4 -> 3 ways
                # candies_left - limit cannot exceed limit
                count += max(limit - (candies_left - limit) + 1, 0)
        return count
        '''


        # -- optimized approach --
        '''
        count = 0
        for i in range(min(limit, n) + 1):
            if n - i > 2 * limit:
                continue
            count += min(n - i, limit) - max(0, n - i - limit) + 1
        return count
        '''


        # -- even more optimized approach --
        return (
            cal(n+2)
            - 3 * cal(n - limit + 1)
            + 3 * cal(n - (limit + 1) * 2 + 2)
            - cal(n - 3 * (limit + 1) + 2)
        )
        
def cal(x):
    if x < 0:
        return 0
    return x * (x - 1) // 2