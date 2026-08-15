class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p = 0

        for r in range(len(nums)):
            if nums[r] != val:
                nums[p] = nums[r]
                p += 1
        return p
        