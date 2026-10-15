class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a, b = {}, {}

        for x, y in trust:
            a[x] = 1 + a.get(x, 0)
            b[y] = 1 + b.get(y, 0)

        for i in range(1, n + 1):
            if i in b and b[i] == n - 1 and i not in a:
                return i
        return -1

        