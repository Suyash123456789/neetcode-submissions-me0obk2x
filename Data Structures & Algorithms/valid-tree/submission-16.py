class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        
        adj = {i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit = set()
        def dfs(i, prev):
            if i in visit:
                return False

            visit.add(i)

            for j in adj[i]:
                if prev == j:
                    continue
                if not dfs(j, i):
                    return False
            return True
        if not dfs(0, -1):
            return False
        return len(visit) == n
