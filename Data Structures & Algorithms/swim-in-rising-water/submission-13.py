class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        visit = set()
        minH = [[grid[0][0], 0, 0]]
        visit.add((0, 0))
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        while minH:
            t, r, c = heapq.heappop(minH) 
            if r == N - 1 and c == N - 1:
                return t
            for dr, dc in directions:
                neiR, neiC = r + dr, c + dc
                if neiR >= 0 and neiR < N and neiC >= 0 and neiC < N and (neiR, neiC) not in visit:
                    heapq.heappush(minH, [max(t, grid[neiR][neiC]), neiR, neiC])
                    visit.add((neiR, neiC))
        