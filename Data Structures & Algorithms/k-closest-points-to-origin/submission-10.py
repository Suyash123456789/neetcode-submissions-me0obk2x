class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[[x**2+y**2,x, y] for x, y in points]
        heapq.heapify(minHeap)

        res=[]
        while len(res)<k:
            d,x,y=heapq.heappop(minHeap)
            res.append([x, y])
        return res