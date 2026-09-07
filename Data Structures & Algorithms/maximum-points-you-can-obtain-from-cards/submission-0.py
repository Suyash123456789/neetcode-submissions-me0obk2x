class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints) <= k:
            return sum(cardPoints)

        right = 0
        curSum = 0
        for r in range(k):
            curSum += cardPoints[r]
            right = r

        res = curSum
        l = 0
        while right >= 0:
            l = (l - 1 + len(cardPoints)) % len(cardPoints)
            curSum -= cardPoints[right]
            right -= 1
            curSum += cardPoints[l]
            res = max(res, curSum)
        return res