# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res=0

        def dfs(node, prevMax):
            if not node:
                return 0
            self.res+=1 if node.val>=prevMax else 0
            dfs(node.left, max(node.val,prevMax))
            dfs(node.right, max(node.val,prevMax))
        dfs(root, float("-inf"))
        return self.res
