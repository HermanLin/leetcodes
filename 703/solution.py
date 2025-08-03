import heapq
from typing import List


'''class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.N = len(nums)
        self.max_heap = []
        self.min_heap = []
        
        for n in nums:
            heapq.heappush(self.min_heap, n)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            if len(self.max_heap) > (self.N - k):
                heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def add(self, val: int) -> int:
        self.N += 1
        heapq.heappush(self.min_heap, val)
        heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        if len(self.max_heap) > (self.N - self.k):
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            
        return self.min_heap[0]'''


# If we don't need to keep in mind any other numbers besides kth
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.min_heap = []
        self.k = k
        
        for n in nums:
            heapq.heappush(self.min_heap, n)
            if len(self.min_heap) > k:
                heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k or self.min_heap[0] < val:
            heapq.heappush(self.min_heap, val)
        
        if len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)
            
        return self.min_heap[0]
