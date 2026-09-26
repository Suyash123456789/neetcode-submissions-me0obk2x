class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        largest = 0
        in_set = set(nums)
        for n in nums:
            if n - 1 not in in_set:
                longest = 0
                while n + longest in in_set:
                    longest += 1
                largest = max(largest, longest)
        return largest