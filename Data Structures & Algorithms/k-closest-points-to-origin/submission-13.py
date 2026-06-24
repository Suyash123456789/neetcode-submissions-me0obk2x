class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for x, y in points:
            dist=x**2+y**2
            minHeap.append([dist, x, y])
        heapq.heapify(minHeap)
        kt=0
        res=[]
        while minHeap and kt<k:
            dist, x, y=heapq.heappop(minHeap)
            res.append([x, y])
            kt+=1
        return res