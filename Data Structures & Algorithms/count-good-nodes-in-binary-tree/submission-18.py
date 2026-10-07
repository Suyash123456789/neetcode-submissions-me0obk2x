# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def dfs(node, prev):
            if not node:
                return
            if node.val >= prev:
                self.res += 1
            dfs(node.left, max(node.val, prev))
            dfs(node.right, max(node.val, prev))
        dfs(root, -101)
        return self.res