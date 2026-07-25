class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        visit=set()
        islands = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            while q:
                row, col = q.popleft()
                for dr, dc in directions:
                    R, C= row + dr, col + dc
                    if R < 0 or R == len(grid) or C < 0 or C == len(grid[0]) or (R, C) in visit or grid[R][C] == "0":
                        continue
                    q.append((R, C))
                    visit.add((R, C))


        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands