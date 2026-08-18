class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        def can_eat(m):
            total = 0
            for p in piles:
                total += math.ceil(p/m)
            return total <= h
        while l <= r:
            m = (l + r) // 2

            if can_eat(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res
