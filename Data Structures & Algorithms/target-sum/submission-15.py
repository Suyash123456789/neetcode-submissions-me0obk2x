class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(i, t):
            if i == len(nums):
                if t == target:
                    return 1
                else:
                    return 0

            if (i, t) in dp:
                return dp[(i, t)]
            
            dp[(i, t)] = dfs(i + 1, t + nums[i]) + dfs(i + 1, t - nums[i])
            return dp[(i, t)]
        return dfs(0, 0)