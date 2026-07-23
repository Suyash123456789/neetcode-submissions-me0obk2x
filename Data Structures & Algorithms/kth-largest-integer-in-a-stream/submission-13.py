class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap , self.k = nums, k
        heapq.heapify(self.minHeap)

        while self.minHeap and len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)


    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        while self.minHeap and len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]

        
