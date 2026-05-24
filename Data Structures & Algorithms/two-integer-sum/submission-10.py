class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}
        for i, a in enumerate(nums):
            if target-a in prevMap:
                return [prevMap[target-a], i]
            prevMap[a]=i
        
