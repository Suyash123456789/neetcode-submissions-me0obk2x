class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        res = []
        def backtrack(i, curStr):
            if i == len(s):
                res.append(" ".join(curStr))
                return
            for j in range(i, len(s)):
                if s[i:j + 1] in wordDict:
                    curStr.append(s[i:j + 1])
                    backtrack(j + 1, curStr)
                    curStr.pop()
        backtrack(0, [])
        return res