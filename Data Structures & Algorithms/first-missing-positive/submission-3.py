class Solution:
    def firstMissingPositive(self, A: List[int]) -> int:
        B=set(A)
        minP=len(A)+1
        for i in range(1, len(A)+2):
            if i not in B:
                minP=min(minP,i)
                return minP

        