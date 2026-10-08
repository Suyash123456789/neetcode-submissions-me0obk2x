class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-s for s in stones]
        heapq.heapify(arr)
        while len(arr) > 1:
            a, b = heapq.heappop(arr), heapq.heappop(arr)
            if a - b:
                heapq.heappush(arr, a - b) 
        return -arr[0] if arr else 0