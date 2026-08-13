class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)

        # Find pivot
        i = n - 2

        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1

        # No pivot -> already largest permutation
        if i < 0:
            nums.reverse()
            return

        # Find smallest number greater than nums[i]
        j = n - 1

        while nums[j] <= nums[i]:
            j -= 1

        # Swap
        nums[i], nums[j] = nums[j], nums[i]

        # Reverse suffix
        nums[i + 1:] = nums[i + 1:][::-1]

        