# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack = root, []
        res = []

        while cur or stack:
            while cur:
                stack.append((cur, True))
                stack.append((cur.right, False))
                cur = cur.left
            node , is_visit = stack.pop()
            if is_visit:
                res.append(node.val)
            else:
                cur = node
        return res
