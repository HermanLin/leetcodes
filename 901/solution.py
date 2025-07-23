class StockSpanner:

    def __init__(self):
        # will contain tuples (price, count) such that
        # `count` represents how many prices this price
        # is greater than or equal to in previous days
        self.stack = []

    def next(self, price: int) -> int:
        count = 1
        while self.stack and self.stack[-1][0] <= price:
            prev_max = self.stack.pop()
            count += prev_max[1]
            
        self.stack.append((price, count))

        return count


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price) 
 
ss = StockSpanner()
print(ss.next(100)) # [100] -> 1
print(ss.next(80))  # [100, 80] -> 1
print(ss.next(60))  # [100, 80, 60] -> 1
print(ss.next(70))  # [100, 80, 70] -> 1 + 1 = 2
print(ss.next(60))  # [100, 80, 70, 60] -> 1
print(ss.next(75))  # [100, 80, 75] -> 1 + 1 + 2 = 4
print(ss.next(85))  # [100, 85] -> 4 + 1 + 1 = 6
