class Solution:
    def isHappy(self, n: int) -> bool:
        visit=set()

        while n not in visit:
            visit.add(n)
            n=self.sumOfSquares(n)
            if n==1:
                return True
        return False


    def sumOfSquares(self, n):
        x=0
        while n:
            x+=(n%10)**2
            n=n//10
        return x