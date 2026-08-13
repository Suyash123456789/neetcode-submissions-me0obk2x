class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        res = 0
        count = 0
        l = 0

        for r in range(len(nums)):
            if nums[r] == 1:
                count += 1
            while (r - l + 1) - count > k:
                if nums[l] == 1:
                    count -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            