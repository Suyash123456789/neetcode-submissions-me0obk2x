class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        posDiag = set()
        negDiag = set()
        self.res = 0
        def backtrack(r):
            if r == n:
                self.res += 1
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue
                posDiag.add(r + c)
                negDiag.add(r - c)
                col.add(c)
                backtrack(r + 1)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                col.remove(c)
        backtrack(0)
        return self.res

        