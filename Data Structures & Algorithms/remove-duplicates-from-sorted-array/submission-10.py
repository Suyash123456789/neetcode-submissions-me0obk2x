class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1

        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[p] = nums[r]
                p += 1
        return p