class Solution:
    def candy(self, nums: List[int]) -> int:
        arr = [1] * len(nums)

        for i in range(1, len(nums)):
            if nums[i - 1] < nums[i]:
                arr[i] = 1 + arr[i - 1]
        
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                arr[i] = max(arr[i], 1 + arr[i + 1])
        return sum(arr)