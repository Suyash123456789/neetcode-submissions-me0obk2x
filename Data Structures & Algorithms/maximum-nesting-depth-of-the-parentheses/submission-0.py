class Solution:
    def maxDepth(self, s: str) -> int:
        res = 0
        stack = []

        for c in s:
            if c == ")":
                stack.pop()

            elif c == "(":
                stack.append("(")
                res = max(res, len(stack))
        return res
        