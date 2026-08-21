# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.res = 0
        self.ans = None

        def dfs(root):
            if not root:
                return None
            if self.ans:
                return None

            dfs(root.left)
            self.res += 1
            if self.res == k:
                self.ans = root.val
                return
            dfs(root.right)
        dfs(root)
        return self.ans
            