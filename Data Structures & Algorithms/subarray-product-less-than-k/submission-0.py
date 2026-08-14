class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        res = 0
        cur_mul = 1
        l = 0

        for r in range(len(nums)):
            cur_mul *= nums[r]

            while l <= r and cur_mul >= k:
                cur_mul = cur_mul // nums[l]
                l += 1
            res += (r - l + 1)
        return res

