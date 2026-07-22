# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, prevMax):
            if not node:
                return 0
            
            res = 1 if node.val >= prevMax else 0
            prevMax = max(node.val, prevMax)
            res += dfs(node.left, prevMax) + dfs(node.right, prevMax)
            return res
        return dfs(root, -101) 