# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur, stack=root, []
        visit=set()
        res=[]

        while cur or stack:
            while cur:
                visit.add(cur)
                stack.append(cur)
                stack.append(cur.right)
                cur=cur.left
            node=stack.pop()
            if node in visit:
                res.append(node.val)
            else:
                cur=node
        return res

