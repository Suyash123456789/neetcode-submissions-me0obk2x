class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def canShip(cap):
            ship = 1
            total = 0
            for w in weights:
                if total + w > cap:
                    ship += 1
                    total = w
                else:
                    total += w
            return ship<=days


        while l <= r:
            cap = (l + r)//2
            if canShip(cap):
                res = min(res, cap)
                r = cap - 1
            else:
                l = cap + 1
        return res