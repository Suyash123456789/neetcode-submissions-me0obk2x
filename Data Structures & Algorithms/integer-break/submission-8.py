class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {1:1}
        def dfs(x):
            if x in dp:
                return dp[x]

            dp[x] = x if x != n else 0
            for i in range(1, x):
                dp[x] = max(dp[x], dfs(i) * dfs(x - i))
           
            return dp[x]
        return dfs(n)