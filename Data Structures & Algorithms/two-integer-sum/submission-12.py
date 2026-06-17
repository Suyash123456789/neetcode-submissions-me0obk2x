class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        preMap={}
        for i, n in enumerate(nums):
            if target-n in preMap:
                return [preMap[target-n], i]
            preMap[n]=i
        