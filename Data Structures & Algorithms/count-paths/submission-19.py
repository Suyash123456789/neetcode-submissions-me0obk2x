class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for r in range(m - 1):
            newR = [1] * n
            for c in range(n - 2, -1, -1):
                newR[c] = row[c] + newR[c + 1]
            row = newR
        return row[0]