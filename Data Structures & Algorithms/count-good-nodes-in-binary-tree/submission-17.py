# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(root, prev):
            if not root:
                return 

            self.res += 1 if root.val >= prev else 0
            dfs(root.left, max(prev, root.val))
            dfs(root.right, max(prev, root.val))
        dfs(root, -101)
        return self.res

            
