class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS=len(heights), len(heights[0])

        minHeap=[[0,0,0]]
        visit=set()
        directions=[[0,1], [1, 0], [0,-1], [-1, 0]]
        while minHeap:
            diff, r, c=heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            visit.add((r, c))
            if r==ROWS-1 and c==COLS-1:
                return diff

            for dr, dc in directions:
                newR, newC=r+dr, c+dc
                if newR<0 or newR==ROWS or newC<0 or newC==COLS or (newR, newC) in visit:
                    continue
                heapq.heappush(minHeap, [max(diff, abs(heights[r][c]-heights[newR][newC])), newR, newC])

