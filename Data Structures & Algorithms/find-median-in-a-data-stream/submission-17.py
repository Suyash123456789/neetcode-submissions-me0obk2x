class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)
        if (self.small and self.large and (-1 * self.small[0]) > self.large[0]):
            n = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * n)
        if len(self.small) + 1 < len(self.large):
            n = heapq.heappop(self.large)
            heapq.heappush(self.small, -1 * n)
        if len(self.small) > len(self.large) + 1:
            n = heapq.heappop(self.small)
            heapq.heappush(self.large, -1 * n)
        

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -1 * self.small[0]
        else:
            return ((-1 * self.small[0]) + self.large[0]) / 2
        
        