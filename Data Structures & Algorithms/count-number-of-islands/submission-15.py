class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows, cols=len(grid), len(grid[0])
        visit=set()
        def bfs(r, c):
            q=deque([(r,c)])
            visit.add((r,c))
            directions=[[0,1], [1,0], [-1, 0], [0,-1]]
            while q:
                r,c=q.popleft()
                for dr, dc in directions:
                    row, col=r+dr, c+dc
                    if row<0 or col<0 or row>=rows or col>=cols or (row, col) in visit or grid[row][col]=="0":
                        continue
                    visit.add((row, col))
                    q.append([row, col])




        res=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1" and (r,c) not in visit:
                    bfs(r,c)
                    res+=1
        return res