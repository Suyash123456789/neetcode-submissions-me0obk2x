class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        time=0
        q=deque()

        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt=heapq.heappop(maxHeap)
                if cnt+1:
                    q.append([cnt+1, time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxHeap, q.popleft()[0])
        return time
