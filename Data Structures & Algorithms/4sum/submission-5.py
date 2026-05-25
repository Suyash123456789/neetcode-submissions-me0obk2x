from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        quad = []

        def kSum(k: int, start: int, target: int):
            if k == 2:
                l, r = start, len(nums) - 1
                while l < r:
                    s = nums[l] + nums[r]
                    if s > target:
                        r -= 1
                    elif s < target:
                        l += 1
                    else:
                        res.append(quad + [nums[l], nums[r]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                return

            for i in range(start, len(nums) - k + 1):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                quad.append(nums[i])
                kSum(k - 1, i + 1, target - nums[i])
                quad.pop()

        kSum(4, 0, target)
        return res