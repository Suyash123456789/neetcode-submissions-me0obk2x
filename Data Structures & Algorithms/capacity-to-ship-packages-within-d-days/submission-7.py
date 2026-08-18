class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            total = 0
            numShips = 1
            for w in weights:
                if total + w > cap:
                    numShips += 1
                    total = 0
                total += w
            return numShips <= days
                


        while l <= r:
            m = (l + r) // 2
            if canShip(m):
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1
        return res