class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevSum={}
        for i, n in enumerate(nums):
            if target-n in prevSum:
                return [prevSum[target-n], i]
            prevSum[n]=i
        