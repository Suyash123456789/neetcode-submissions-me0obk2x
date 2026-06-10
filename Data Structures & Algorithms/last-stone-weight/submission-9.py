class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        minHeap=[-s for s in stones]
        heapq.heapify(minHeap)
        while len(minHeap)>1:
            x, y=heapq.heappop(minHeap),heapq.heappop(minHeap)
            diff=x-y
            if diff<0:
                heapq.heappush(minHeap, diff)
        return -1*minHeap[0] if minHeap else 0
