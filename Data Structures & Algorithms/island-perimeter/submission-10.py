class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        visit = set()
        ROWS, COLS = len(grid), len(grid[0])
        def dfs(r, c):
            if (r, c) in visit:
                return 0
            if r < 0 or c < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 1

            visit.add((r, c))
            return dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
        
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in visit and grid[r][c]:
                    return dfs(r, c)