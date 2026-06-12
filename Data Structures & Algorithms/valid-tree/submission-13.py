class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adj={i:[] for i in range(n)}
        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)
        visit=set()
        def dfs(crs, prev):
            if crs in visit:
                return False
            visit.add(crs)
            for pre in adj[crs]:
                if pre==prev:
                    continue

                if not dfs(pre, crs):
                    return False
            return True
        return dfs(0,-1) and len(visit)==n
            
