class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minP, maxP = nums[0], nums[0]

        for n in nums[1:]:
            if n == 0:
                res = max(res, n)
                minP, maxP = 1, 1
                continue
            temp = minP
            minP = min(n, minP * n, maxP * n)
            maxP = max(n, temp * n, maxP * n)
            res = max(res, maxP)
        return res

