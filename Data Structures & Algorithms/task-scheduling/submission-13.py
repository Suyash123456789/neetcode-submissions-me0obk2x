class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        time = 0

        while maxHeap or q:
            time += 1

            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                if cnt + 1:
                    q.append([cnt + 1, time + n])
            
            if q and q[0][1] == time:
                c, _ = q.popleft()
                heapq.heappush(maxHeap, c)
        return time