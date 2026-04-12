class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        # Create DP table
        cache = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            cache[i][n] = m - i

        for j in range(n + 1):
            cache[m][j] = n - j

        # Fill table bottom-up
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i + 1][j + 1]
                else:
                    cache[i][j] = 1 + min(
                        cache[i + 1][j],     # delete
                        cache[i][j + 1],     # insert
                        cache[i + 1][j + 1]  # replace
                    )

        return cache[0][0]