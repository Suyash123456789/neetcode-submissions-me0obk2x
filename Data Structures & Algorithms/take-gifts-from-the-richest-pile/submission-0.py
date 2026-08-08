from math import sqrt
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-g for g in gifts]
        heapq.heapify(gifts)
        for _ in range(k):
            n = abs(heapq.heappop(gifts))
            heapq.heappush(gifts, -int(sqrt(n)))
        return - sum(gifts)