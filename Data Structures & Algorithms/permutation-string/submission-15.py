
from collections import defaultdict

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        countS1, countS2 = defaultdict(int), defaultdict(int)

        for i in range(len(s1)):
            countS1[s1[i]] += 1
            countS2[s2[i]] += 1

        if countS1 == countS2:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            countS2[s2[r]] += 1

            countS2[s2[l]] -= 1

            if countS2[s2[l]] == 0:
                del countS2[s2[l]]

            l += 1

            if countS1 == countS2:
                return True

        return False