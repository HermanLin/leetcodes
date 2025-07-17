from typing import List
from collections import defaultdict

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        '''
        digit_sums = defaultdict(list)

        for n in nums:
            x = n
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            digit_sums[total].append(n)

        max_pairsum = -1
        for k in digit_sums:
            vals = digit_sums[k]

            if len(vals) > 1:
                # get the largest two numbers
                vals.sort()
                max_pairsum = max(max_pairsum, vals[-1] + vals[-2])

        return max_pairsum
        '''

        # improved solution, 
        # only track the largest number seen so far.
        # also, reduces complexity by removing sorting requirement
        def getDigitSum(x):
            total = 0
            while x > 0:
                total += x % 10
                x //= 10
            return total

        digit_sums = defaultdict(int)

        ans = -1
        for n in nums:
            digit_sum = getDigitSum(n)
            if digit_sum in digit_sums:
                ans = max(ans, n + digit_sums[digit_sum])
            digit_sums[digit_sum] = max(n, digit_sums[digit_sum])

        return ans
    
sol = Solution()
print(sol.maximumSum([18,43,36,13,7]))
print(sol.maximumSum([81,43,36,13,7,18]))
print(sol.maximumSum([10,12,19,14]))
print(sol.maximumSum([4]))
print(sol.maximumSum([5,1,6]))
print(sol.maximumSum([4,6,10,6]))
print(sol.maximumSum([2,1,5,5,2,4]))
print(sol.maximumSum([368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183]))
print(sol.maximumSum([229,398,269,317,420,464,491,218,439,153,482,169,411,93,147,50,347,210,251,366,401]))
print(sol.maximumSum([809039901,892618095,699694397,576724044,699515542,831899037,959450091,88124465,102780641,275884357,658771111,660539885,620862925,263622781,778473545,672947452,521367711,970040373,895455228,886907524,781592735,528179525,100136578,646624289,523918444,628999419,931048268,991029445,631668102,667259810,535380751,786735115,971553625,797004919,81520773,137283330,846189211,464238688,713970439,286355524,482704479,527261737,383453409,217307241,601715229,828501551,256079369,567779582,770290899,264325638,778183437,411538949,798508462,831231181,56846075,112379513,259195786,67218178,957517878,911879358,119232266,891855628,438001321,732866407,521986754,5058581,912946383,243362613,899499777,226815070,285361727,44274463]))