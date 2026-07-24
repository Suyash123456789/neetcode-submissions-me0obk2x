from typing import List

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        dp = {}

        def dfs(i: int, total: int) -> int:
            if i == len(nums):
                return total

            if (i, total) in dp:
                return dp[(i, total)]

            include = dfs(i + 1, total ^ nums[i])
            exclude = dfs(i + 1, total)

            dp[(i, total)] = include + exclude
            return dp[(i, total)]

        return dfs(0, 0)