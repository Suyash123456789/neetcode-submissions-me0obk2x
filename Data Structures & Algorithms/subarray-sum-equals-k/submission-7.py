class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        curSum = 0
        preSum = {0 : 1}
        res = 0

        for n in nums:
            curSum += n
            if curSum - k in preSum:
                res += preSum[curSum - k] 
            if curSum not in preSum:
                preSum[curSum] = 0
            preSum[curSum] += 1
        return res
            