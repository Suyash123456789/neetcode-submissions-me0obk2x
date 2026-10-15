class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderInd = {}
        for i, c in enumerate(order):
            orderInd[c] = i

        for i in range(len(words) - 1):
            minLen = min(len(words[i]), len(words[i + 1]))
            if len(words[i]) > len(words[i + 1]) and words[i][:minLen] == words[i + 1][:minLen]:
                return False
            for j in range(minLen):
                if words[i][j] != words[i + 1][j]:
                    if orderInd[words[i][j]] > orderInd[words[i + 1][j]]:
                        return False
                    break
        return True