class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = heapq.heappop(maxHeap)
                cnt = cnt + 1
                if cnt:
                    q.append([cnt, time + n])
                
            if q and time == q[0][1]:
                c, t = q.popleft()
                heapq.heappush(maxHeap, c)
        return time

