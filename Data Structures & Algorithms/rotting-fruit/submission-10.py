class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque()
        time, fresh=0,0
        ROWS, COLS=len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c]==2:
                    q.append((r, c))
                elif grid[r][c]==1:
                    fresh+=1

        while q and fresh > 0:
            for i in range(len(q)):
                row, col=q.popleft()
                directions=[[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    r,c=row+dr, col+dc
                    if r<0 or c<0 or r>=ROWS or c>=COLS or grid[r][c]!=1:
                        continue
                    grid[r][c]=2
                    fresh-=1
                    q.append((r,c))
            time+=1
        return time if not fresh else -1
                    