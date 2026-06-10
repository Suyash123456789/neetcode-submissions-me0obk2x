class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate(tasks):
            t.append(i)
        tasks.sort(key=lambda t:t[0])

        res, minHeap=[],[]
        i, time=0, tasks[0][0]

        while i<len(tasks) or minHeap:
            while i< len(tasks) and tasks[i][0]<=time:
                heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
                i+=1
            if not minHeap:
                time=tasks[i][0]
            else:
                p, index=heapq.heappop(minHeap)
                time+=p
                res.append(index)
        return res
