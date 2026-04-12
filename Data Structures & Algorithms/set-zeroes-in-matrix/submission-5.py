class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROWS,COLS=len(matrix), len(matrix[0])
        is_zero=False

        for i in range(ROWS):
            for j in range(COLS):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i>0:
                        matrix[i][0]=0
                    else:
                        is_zero=True
        for r in range(1,ROWS):
            for c in range(1, COLS):
                if matrix[0][c]==0 or matrix[r][0]==0:
                    matrix[r][c]=0

        if matrix[0][0]==0:
            for r in range(ROWS):
                matrix[r][0]=0
        if is_zero:
            for c in range(COLS):
                matrix[0][c]=0
                


        

