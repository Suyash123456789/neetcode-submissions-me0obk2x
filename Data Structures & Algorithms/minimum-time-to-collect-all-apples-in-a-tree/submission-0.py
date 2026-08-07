class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = { i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        def dfs(cur, par):
            time = 0

            for child in adj[cur]:
                if child == par:
                    continue
                childTime = dfs(child, cur)
                if childTime or hasApple[child]:
                    time += 2 + childTime
            return time
        return dfs(0, -1)

        
