class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x, y in points:
            dist=x*x+y*y
            heapq.heappush(minHeap, [dist, x, y])
        c=0
        res=[]
        while c!=k:
            d,x,y=heapq.heappop(minHeap)
            res.append([x,y])
            c+=1
        return res
