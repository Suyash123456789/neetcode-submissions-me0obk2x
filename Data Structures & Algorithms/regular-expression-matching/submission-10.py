class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cache = {}

        def dfs(i, j):
            if (i, j) in cache:
                return cache[(i, j)]

            # both strings consumed
            if i >= len(s) and j >= len(p):
                return True

            # pattern consumed but string not
            if j >= len(p):
                return False

            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            if (j + 1) < len(p) and p[j + 1] == "*":
                # skip "x*" OR use it if match
                cache[(i, j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            elif match:
                cache[(i, j)] = dfs(i + 1, j + 1)
            else:
                cache[(i, j)] = False

            return cache[(i, j)]

        return dfs(0, 0)