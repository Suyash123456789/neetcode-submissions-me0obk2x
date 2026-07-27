class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        visit.add((0, 0))

        while minH:
            t, r, c = heapq.heappop(minH)

            if r == N - 1 and c == N - 1:
                return t
            
            for dr, dc in directions:
                row, col = dr + r, dc + c
                if row < 0 or col < 0 or row == N or col == N or (row, col) in visit:
                    continue
                heapq.heappush(minH, [max(t, grid[row][col]), row, col])
                visit.add((row, col))
        