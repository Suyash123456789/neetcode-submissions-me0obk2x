class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        
        nums = [0] + flowerbed + [0]

        # [0,1,0,0,0,0,1,0]

        for i in range(1, len(nums) - 1):
            if nums[i] == 0 and nums[i - 1] == 0 and nums[i + 1] == 0:
                nums[i] = 1
                n -= 1
                if n == 0:
                    return True
        return True if n == 0 else False
 
        
