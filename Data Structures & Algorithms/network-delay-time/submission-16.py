class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visit = set()
        minH = [(0, k)]
        res = 0
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        while minH:
            t, n0 = heapq.heappop(minH)
            if n0 in visit:
                continue
            visit.add(n0)
            res = max(res, t)
            for n1, t1 in adj[n0]:
                if n1 not in visit:
                    heapq.heappush(minH, (t + t1, n1))
        return res if len(visit) == n else -1 