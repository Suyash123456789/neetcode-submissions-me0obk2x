class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(numRows - 1):
            n = [0] + res[-1] + [0]
            num = []
            for j in range(len(res[-1]) + 1):
                num.append(n[j] + n[j + 1])
            res.append(num)
        return res