# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        cur = root

        while cur or stack:
            while cur:
                stack.append([cur, True])
                stack.append([cur.right, False])
                cur = cur.left
            if stack:
                node, to_append = stack.pop()
                if node and to_append:
                    res.append(node.val)
                else:
                    cur = node
        return res
        
