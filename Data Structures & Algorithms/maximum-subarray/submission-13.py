class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = max(nums)
        curSum = 0

        for n in nums:
            curSum+=n
            if curSum<0:
                curSum=0
                continue
            maxSub= max(maxSub, curSum)
        return maxSub