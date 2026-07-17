from typing import List


class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.sum_mat = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            row_prefix = 0
            for c in range(cols):
                row_prefix += matrix[r][c]
                above = self.sum_mat[r][c + 1]
                self.sum_mat[r + 1][c + 1] = row_prefix + above

    def sumRegion(
        self,
        row1: int,
        col1: int,
        row2: int,
        col2: int,
    ) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        bottom_right = self.sum_mat[row2][col2]
        above = self.sum_mat[row1 - 1][col2]
        left = self.sum_mat[row2][col1 - 1]
        top_left = self.sum_mat[row1 - 1][col1 - 1]

        return bottom_right - above - left + top_left