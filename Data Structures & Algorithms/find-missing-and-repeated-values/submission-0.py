class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        count = defaultdict(int)

        for i in range(N):
            for j in range(N):
                count[grid[i][j]] += 1
        double, missing = 0, 0
        for nums in range(1, N*N + 1):
            if count[nums] == 0:
                missing = nums
            if count[nums] == 2:
                double = nums
        return [double, missing]
