class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        dp = {}
        dp[len(stoneValue)] = 0
        def dfs(i):
            if i in dp:
                return dp[i]
            res = float("-inf")
            total = 0
            for j in range(i, min(i + 3, len(stoneValue))):
                total += stoneValue[j] 
                res = max(res, total - dfs(j + 1)) 
            dp[i] = res
            return res
        x = dfs(0)  
        if x < 0:
            return "Bob"
        elif x > 0:
            return "Alice"
        else:
            return "Tie"