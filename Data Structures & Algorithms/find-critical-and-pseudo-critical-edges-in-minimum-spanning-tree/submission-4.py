from typing import List


class UnionFind:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, node: int) -> int:
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def union(self, node1: int, node2: int) -> bool:
        root1 = self.find(node1)
        root2 = self.find(node2)

        if root1 == root2:
            return False

        if self.size[root1] < self.size[root2]:
            root1, root2 = root2, root1

        self.parent[root2] = root1
        self.size[root1] += self.size[root2]
        return True


class Solution:
    def findCriticalAndPseudoCriticalEdges(
        self,
        n: int,
        edges: List[List[int]]
    ) -> List[List[int]]:

        indexed_edges = [
            [u, v, weight, index]
            for index, (u, v, weight) in enumerate(edges)
        ]
        indexed_edges.sort(key=lambda edge: edge[2])

        def kruskal(
            excluded_edge: int = -1,
            included_edge: int = -1
        ) -> float:
            uf = UnionFind(n)
            total_weight = 0
            edges_used = 0

            # Force an edge into the MST.
            if included_edge != -1:
                u, v, weight, _ = indexed_edges[included_edge]
                if uf.union(u, v):
                    total_weight += weight
                    edges_used += 1

            for edge_index, (u, v, weight, _) in enumerate(indexed_edges):
                if edge_index == excluded_edge:
                    continue

                if uf.union(u, v):
                    total_weight += weight
                    edges_used += 1

                    if edges_used == n - 1:
                        break

            if edges_used != n - 1:
                return float("inf")

            return total_weight

        mst_weight = kruskal()
        critical = []
        pseudo_critical = []

        for edge_index, (_, _, _, original_index) in enumerate(indexed_edges):
            # Removing the edge makes the MST heavier or impossible.
            if kruskal(excluded_edge=edge_index) > mst_weight:
                critical.append(original_index)

            # Forcing the edge still allows an MST with optimal weight.
            elif kruskal(included_edge=edge_index) == mst_weight:
                pseudo_critical.append(original_index)

        return [critical, pseudo_critical]