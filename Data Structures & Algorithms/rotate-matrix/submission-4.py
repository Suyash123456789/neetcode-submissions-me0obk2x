from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        l, r = 0, len(matrix) - 1
        
        while l < r:
            for i in range(r - l):
                top, bottom = l, r
                
                # save top-left
                topLeft = matrix[top][l + i]
                
                # move bottom-left → top-left
                matrix[top][l + i] = matrix[bottom - i][l]
                
                # move bottom-right → bottom-left
                matrix[bottom - i][l] = matrix[bottom][r - i]
                
                # move top-right → bottom-right
                matrix[bottom][r - i] = matrix[top + i][r]
                
                # move saved top-left → top-right
                matrix[top + i][r] = topLeft
            
            r -= 1
            l += 1