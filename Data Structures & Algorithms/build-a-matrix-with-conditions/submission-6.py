class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def dfs(src, adj, visit, path, order):
            if src in path:
                return False
            if src in visit:
                return True
            visit.add(src)
            path.add(src)

            for nei in adj[src]:
                if not dfs(nei, adj, visit, path, order):
                    return False
            
            order.append(src)
            path.remove(src)
            return True

        def topo_sort(edges):
            adj = defaultdict(list)
            for src, dst in edges:
                adj[src].append(dst)
            visit, path = set(), set()
            order = []
            for src in range(1, k + 1):
                if not dfs(src, adj,visit, path, order):
                    return []
            return order[::-1]

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []
        res = [[0] * k for _ in range(k)]
        for num in range(1, k + 1):
            r = row_order.index(num)
            c = col_order.index(num)
            res[r][c] = num
        return res