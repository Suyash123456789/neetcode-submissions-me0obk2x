class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        dp = {}
        def dfs(r, c):
            if r == ROWS - 1 and c == COLS - 1:
                return grid[ROWS - 1][COLS - 1]
            if r < 0 or c < 0 or r == ROWS or c == COLS:
                return float("inf")
            if (r, c) in dp:
                return dp[(r, c)]

            dp[(r, c)] = grid[r][c] + min(dfs(r + 1, c), dfs(r, c + 1))
            return dp[(r, c)]

        return dfs(0, 0)