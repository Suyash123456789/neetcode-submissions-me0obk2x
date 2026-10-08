# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = 0
        ans = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.res += 1
            if self.res == k:
                ans.append(node.val)
            dfs(node.right)
        dfs(root)
        if ans:
            return ans[0]
        return -1
                