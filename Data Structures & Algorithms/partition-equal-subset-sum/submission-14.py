class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False

        target = total // 2
        dp = {}
        def dfs(i, total):
            if total == 0:
                return True
            if total < 0 or i == len(nums):
                return False
            if (i, total) in dp:
                return dp[(i, total)]

            dp[(i, total)] = dfs(i + 1, total - nums[i]) or dfs(i + 1, total)
            return dp[(i, total)]
        return dfs(0, target)