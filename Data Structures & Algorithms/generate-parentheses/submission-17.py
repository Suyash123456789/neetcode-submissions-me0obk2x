class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(openN, closedN, cur):
            if openN == closedN == n:
                res.append("".join(cur.copy()))
                return
            
            if openN < n:
                cur.append("(")
                dfs(openN + 1, closedN, cur)
                cur.pop()
            if closedN < openN:
                cur.append(")")
                dfs(openN, closedN + 1, cur)
                cur.pop()
        dfs(0, 0, [])
        return res