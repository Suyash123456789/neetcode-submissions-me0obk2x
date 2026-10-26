from math import ceil
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        total = sum(stones)
        target = ceil(total / 2)
       
        dp = {}

        def dfs(i, t):
            if t >= target or i == len(stones):
                return abs(t - (total - t))
                
            if (i, t) in dp:
                return dp[(i, t)]
            dp[(i, t)] = min(dfs(i + 1, t + stones[i]), dfs(i + 1, t))
            return dp[(i, t)]

        return dfs(0, 0)
        
