"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def dfs(n, r, c):
            allSame = True
            for i in range(n):
                for j in range(n):
                    if grid[r + i][c + j] != grid[r][c]:
                        allSame = False
                        break
                if not allSame:
                    break
            if allSame:
                return Node(grid[r][c], True)
            
            n = n // 2
            topL = dfs(n, r, c)
            topR = dfs(n, r, c + n)
            bottomL = dfs(n, r + n, c)
            bottomR = dfs(n, r + n, c + n)
            return Node(0, False, topL, topR, bottomL, bottomR)
        return dfs(len(grid), 0, 0)