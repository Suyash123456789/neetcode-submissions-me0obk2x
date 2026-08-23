class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res, maxHeap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count:
                maxHeap.append([count, char])
        heapq.heapify(maxHeap)
        
        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) >= 2 and res[-1] == res[-2] == char:
                if not maxHeap:
                    return res
                cnt, ch = heapq.heappop(maxHeap)
                res += ch
                cnt += 1
                if cnt:
                    heapq.heappush(maxHeap, [cnt, ch])
            res += char
            count += 1
            if count:
                heapq.heappush(maxHeap, [count, char])
        return res

