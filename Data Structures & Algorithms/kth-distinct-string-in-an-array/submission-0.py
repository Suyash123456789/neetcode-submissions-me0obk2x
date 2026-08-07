from collections import Counter

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = Counter(arr)

        res = []

        for s in arr:
            if count[s] == 1:
                res.append(s)

        if len(res) < k:
            return ""

        return res[k - 1]