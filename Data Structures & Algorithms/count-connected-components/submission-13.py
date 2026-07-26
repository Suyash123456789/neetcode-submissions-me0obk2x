class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        ranks = [1] * n

        def find(n1):
            res = n1

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res

        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return 0

            if ranks[p1] > ranks[p2]:
                par[p2] = par[p1]
                ranks[p1] += ranks[p2]
            else:
                par[p1] = par[p2]
                ranks[p2] += ranks[p1]
            return 1

        total = n
        for n1, n2 in edges:
            total -= union(n1, n2)
        return total