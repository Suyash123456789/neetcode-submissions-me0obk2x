class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(cap):
            total = 0
            split = 1
            for n in nums:
                if total + n > cap:
                    total = 0
                    split += 1
                total += n
            return split <= k

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = (l + r) // 2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res