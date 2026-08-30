class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {len(stoneValue):0}
        def dfs(i):
            if i in dp:
                return dp[i]


            res = float("-inf")
            total = 0
            for j in range(i, min(len(stoneValue), i + 3)):
                total += stoneValue[j]
                res = max(res, total - dfs(j + 1))
            dp[i] = res
            return res
        n = dfs(0)
        if n > 0:
            return "Alice"
        elif n < 0:
            return "Bob"
        elif n == 0:
            return "Tie"
            
        
