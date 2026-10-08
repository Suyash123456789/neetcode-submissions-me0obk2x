class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pts = [[x**2 + y**2, x, y] for x, y in points]
        heapq.heapify(pts)
        res = []
        while k and pts:
            p, x, y = heapq.heappop(pts)
            res.append([x, y])
            k -= 1
        return res
            