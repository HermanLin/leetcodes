class Solution:
    def maximum69Number (self, num: int) -> int:
        '''str_num = str(num)
        
        for i in range(len(str_num)):
            if str_num[i] == "6":
                return int(str_num[:i] + "9" + str_num[i+1:])
                           
        return num'''

        # pure math approach
        N = len(str(num))

        for i in range(N):
            d = (num // (10 ** (N - i - 1))) % 10
            if d == 6:
                left = num - (num % (10 ** (N - i)))
                right = num % (10 ** (N - i - 1))
                return left + (9 * (10 ** (N - i - 1))) + right

        return num

sol = Solution() 
print(sol.maximum69Number(9669))
print(sol.maximum69Number(9996))
print(sol.maximum69Number(9999))
print(sol.maximum69Number(6999))
