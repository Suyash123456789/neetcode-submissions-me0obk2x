class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones=[-s for s in stones]
        heapq.heapify(stones)

        while len(stones)>1:
            a, b=heapq.heappop(stones),heapq.heappop(stones)
            if a-b:
                heapq.heappush(stones,a-b)
        return -1*stones[0] if stones else 0