class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        dp = {(ROWS - 1, COLS - 1): grid[ROWS - 1][COLS - 1]}
        def dfs(r, c):
            if (r, c) in visit or r < 0 or c < 0 or r >= ROWS or c >= COLS:
                return float("inf")
            if (r, c) in dp:
                return dp[(r, c)]
            visit.add((r, c))
            res = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            visit.remove((r, c))
            dp[(r, c)] = res
            return res
        return dfs(0, 0)