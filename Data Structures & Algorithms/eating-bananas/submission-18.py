from math import ceil
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = -1
        while l <= r:
            m = (l + r) // 2
            total = 0
            for p in piles:
                total += ceil(p/m)
            if total > h:
                l = m + 1
            else:
                res = m
                r = m - 1
        return res