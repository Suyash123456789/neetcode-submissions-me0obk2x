class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS, countT = Counter(s), Counter(t)
        for k, v in countS.items():
            if v != countT.get(k, 0):
                return False
        return True
