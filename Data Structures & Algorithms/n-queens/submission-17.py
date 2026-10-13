class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        chess = [["."] * n for r in range(n)]
        sameCol = set()
        posDiag = set()
        negDiag = set()
        res = []

        def dfs(r):
            if r == n:
                copy = ["".join(row) for row in chess]
                res.append(copy)
                return
            
            for c in range(n):
                if c not in sameCol and (r + c) not in posDiag and (r - c) not in negDiag:
                    chess[r][c] = "Q"
                    sameCol.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    dfs(r + 1)
                    chess[r][c] = "."
                    sameCol.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
        dfs(0)
        return res

