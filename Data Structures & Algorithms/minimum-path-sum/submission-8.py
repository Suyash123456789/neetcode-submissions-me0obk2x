class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        row = [0] * COLS
        row[-1] = grid[ROWS - 1][COLS - 1]
        for c in range(COLS - 2, -1, -1):
            row[c] = grid[ROWS - 1][c] + row[c + 1]
        
        
        for r in range(ROWS - 2, -1, -1):
            for c in range(COLS - 1, -1, -1):
                if (c + 1) < COLS:
                    row[c] = grid[r][c] + min(row[c], row[c + 1])
                else:
                    row[c] += grid[r][c]
        return row[0]

                