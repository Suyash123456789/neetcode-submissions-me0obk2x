class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            while q:
                row, col = q.popleft()
                for dr, dc in directions:

                    ro, co = row + dr, col + dc
                    if ro < 0 or ro == rows or co < 0 or co == cols or grid[ro][co] == "0" or (ro, co) in visit:
                        continue
                    q.append((ro, co))
                    visit.add((ro, co))




        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    bfs(r, c)
        return islands
