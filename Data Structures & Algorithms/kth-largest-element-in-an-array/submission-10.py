import random

class Solution:
    def findKthLargest(self, nums, k):
        target = len(nums) - k
        left, right = 0, len(nums) - 1

        while left <= right:
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot = nums[right]

            p = left
            for i in range(left, right):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1

            nums[p], nums[right] = nums[right], nums[p]

            if p == target:
                return nums[p]
            elif p < target:
                left = p + 1
            else:
                right = p - 1