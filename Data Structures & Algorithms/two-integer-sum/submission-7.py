class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}

        for i, v in enumerate(nums):
            if target-v in prevMap:
                return [prevMap[target-v], i]
            prevMap[v]=i

            
        

        
