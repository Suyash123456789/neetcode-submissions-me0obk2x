class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visit = set()
        def dfs(r, c):
            if r < 0 or c < 0 or r == N or c == N or (r, c) in visit or not grid[r][c]:
                return

            visit.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        def bfs(visit):
            res, q = 0, deque(visit)
            while q:
                for i in range(len(q)):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        curR, curC = r + dr, c + dc
                        if curR < 0 or curC < 0 or curR == N or curC == N or (curR, curC) in visit:
                            continue
                        if grid[curR][curC]:
                            return res
                        q.append([curR, curC])
                        visit.add((curR, curC))
                res += 1
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs(visit)
            
