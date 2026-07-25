class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        incoming = defaultdict(int)
        outgoing = defaultdict(int)

        for src, dst in trust:
            incoming[dst] += 1
            outgoing[src] += 1

        for i, t in incoming.items():
            if t == n - 1 and outgoing[i] == 0:
                return i
        return -1