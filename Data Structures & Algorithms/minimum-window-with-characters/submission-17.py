class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countS, countT = {}, {}
        if len(s) < len(t):
            return ""
        for i in range(len(t)):
            countT[t[i]] = 1 + countT.get(t[i], 0)
        have, need = 0, len(countT)
        resLen = float("inf")
        res = [-1, -1]
        l = 0
        for r in range(len(s)):
            countS[s[r]] = 1 + countS.get(s[r], 0)
            if countS[s[r]] == countT.get(s[r], 0):
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = [l, r]
                countS[s[l]] -= 1
                if countS[s[l]] < countT.get(s[l], 0):
                    have -= 1
                l += 1
        return s[res[0]:res[1] + 1] if resLen != float("inf") else ""
        
        