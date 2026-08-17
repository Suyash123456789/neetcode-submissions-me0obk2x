class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        countT, window = {}, {}

        for c in t:
            countT[c] = 1 + countT.get(c, 0)

        have, need = 0, len(countT)
        l = 0
        resLen, res = float("inf"), ""
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)
            if window[c] == countT.get(c, 0):
                have += 1
            while have == need:
                if (r - l + 1) < resLen:
                    resLen = r - l + 1
                    res = s[l:r+1]
                window[s[l]] -= 1
                if window[s[l]] < countT.get(s[l], 0):
                    have -= 1
                l += 1
        return res