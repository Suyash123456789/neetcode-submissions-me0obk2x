class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        time, fresh = 0, 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    fresh += 1 
                if grid[r][c] == 2:
                    q.append([r, c])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    newR, newC = r + dr, c + dc
                    if 0 <= newR < ROWS and 0 <= newC < COLS and grid[newR][newC] == 1:
                        grid[newR][newC] = 2
                        q.append([newR, newC])
                        fresh -= 1
            time += 1
        return time if not fresh else -1
