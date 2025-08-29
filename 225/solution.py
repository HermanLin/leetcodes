from collections import deque

# two-queue solution
class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self.q2.append(x)

        while len(self.q1):
            self.q2.append(self.q1.popleft())

        temp = self.q1
        self.q1 = self.q2
        self.q2 = temp
        
        return

    def pop(self) -> int:
        if len(self.q1):
            return self.q1.popleft()
        return 0

    def top(self) -> int:
        if len(self.q1):
            return self.q1[0]
        return 0

    def empty(self) -> bool:
        return len(self.q1) == 0

# one-queue solution
class MyOtherStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        n = len(self.q)

        self.q.append(x)

        for _ in range(n):
            self.q.append(self.q.popleft())

        return

    def pop(self) -> int:
        if len(self.q):
            return self.q.popleft()
        return 0

    def top(self) -> int:
        if len(self.q):
            return self.q[0]
        return 0

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
