class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r=max(weights), sum(weights)
        res=r

        def canShip(cap):
            ships, currCap=1, 0
            for w in weights:
                if currCap+w>cap:
                    ships+=1
                    currCap=0
                currCap+=w
            return ships<=days


        while l<=r:
            cap=(l+r)//2
            if canShip(cap):
                res=cap
                r=cap-1
            else:
                l=cap+1
        return res
