class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = {}
        def dfs(i, j, k):
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in dp:
                return dp[(i, j)]
            
            if i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j, k + 1):
                dp[(i, j)] = True
            elif j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1, k + 1):
                dp[(i, j)] = True
            else:
                dp[(i, j)] = False
            return dp[(i, j)]
        return dfs(0, 0, 0)