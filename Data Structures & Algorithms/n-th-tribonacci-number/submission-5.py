class Solution:
    def tribonacci(self, n: int) -> int:
        tri = [0, 1, 1]

        if n < 3:
            return tri[n]
        
        for i in range(3, n + 1):
            temp = tri[0] + tri[1] + tri[2]
            tri[0] = tri[1]
            tri[1] = tri[2]
            tri[2] = temp
        return tri[2]