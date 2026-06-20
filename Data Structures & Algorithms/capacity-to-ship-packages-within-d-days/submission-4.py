class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r=max(weights), sum(weights)
        res=r

        def canShip(cap):
            ship=1
            cur=cap
            for w in weights:
                if cur-w<0:
                    ship+=1
                    cur=cap
                cur-=w
            return ship<=days

        while l<=r:
            cap=(l+r)//2
            if canShip(cap):
                res=cap
                r=cap-1
            else:
                l=cap+1
        return res