class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q=deque()
        time=0
        while maxHeap or q:
            time+=1
            
            if maxHeap:
                x=heapq.heappop(maxHeap)
                if x and x+1!=0:
                    q.append([x+1, time+n])
            if q and q[0][1]==time:
                c, a=q.popleft()
                heapq.heappush(maxHeap, c)
        return time
