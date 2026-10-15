class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()
        def dfs(r, c, dup, prev):
            if (r, c) in dup  or r < 0 or c < 0 or r == ROWS or c == COLS or heights[r][c] < prev:
                return 
            dup.add((r, c))
            dfs(r + 1, c, dup, heights[r][c])
            dfs(r - 1, c, dup, heights[r][c])
            dfs(r, c + 1, dup, heights[r][c])
            dfs(r, c - 1, dup, heights[r][c])
        
        for c in range(COLS):
            dfs(0, c, pac, -1)
            dfs(ROWS - 1, c, atl, -1)

        for r in range(ROWS):
            dfs(r, 0, pac, -1)
            dfs(r, COLS - 1, atl, -1)
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res