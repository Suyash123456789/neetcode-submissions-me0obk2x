class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r
        while l <= r:
            m = (l + r)//2
            if not self.canShip(weights, m, days):
                l = m + 1
            else:
                res = m
                r = m - 1
        return res



    def canShip(self, weights, m, k):

        total = 1
        cap = 0
        for w in weights:
            if cap + w > m:
                cap = 0
                total += 1
            cap += w
        return total <= k