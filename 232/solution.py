class MyQueue:

    def __init__(self):
        self.queue = []
        self.helper = []

    def push(self, x: int) -> None:
        while len(self.queue):
            self.helper.append(self.queue.pop())

        self.queue.append(x)
        
        while len(self.helper):
            self.queue.append(self.helper.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
    
# amortized O(1) operations
class MyQueue2:

    def __init__(self):
        self.enqueue = []
        self.dequeue = []

    def push(self, x: int) -> None:
        self.enqueue.append(x)

    def pop(self) -> int:
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())

        return self.dequeue.pop()

    def peek(self) -> int:
        if not self.dequeue:
            while self.enqueue:
                self.dequeue.append(self.enqueue.pop())

        return self.dequeue[-1]

    def empty(self) -> bool:
        return max(len(self.enqueue), len(self.dequeue)) == 0

