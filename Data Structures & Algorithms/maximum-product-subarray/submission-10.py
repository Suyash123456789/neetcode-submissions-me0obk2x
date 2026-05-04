class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        curMin, curMax=1, 1

        for n in nums:
            if n==0:
                curMax, curMin=1,1
                continue
            tmp=curMax*n
            curMax=max(n*curMin, n*curMax, n)
            curMin=min(n*curMin, tmp, n)
            res=max(res, curMax)
        return res
            