class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
        self.w = w
        

    def pickIndex(self) -> int:
        n = random.randint(1, self.w[-1])
        
        l, r = 0, len(self.w) - 1

        while l <= r:
            m = l + (r - l) // 2
            if self.w[m] < n:
                l = m + 1
            else:
                r = m - 1
        return l

        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()