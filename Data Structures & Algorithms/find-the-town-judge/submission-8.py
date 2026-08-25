class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            outgoing[src] += 1
            incoming[dst] += 1
        
        for i in range(n + 1):
            if incoming[i] == n - 1 and outgoing[i] == 0:
                return i
        return -1