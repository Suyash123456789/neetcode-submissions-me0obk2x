class Solution:
    def totalNQueens(self, n: int) -> int:
        chess = [["."] * n for r in range(n)]
        sameCol = set()
        posDiag = set()
        negDiag = set()
        self.res = 0

        def dfs(r):
            if r == n:
                self.res += 1
                return
            
            for c in range(n):
                if c not in sameCol and (r + c) not in posDiag and (r - c) not in negDiag:
                    
                    sameCol.add(c)
                    posDiag.add(r + c)
                    negDiag.add(r - c)
                    dfs(r + 1)
                   
                    sameCol.remove(c)
                    posDiag.remove(r + c)
                    negDiag.remove(r - c)
        dfs(0)
        return self.res

