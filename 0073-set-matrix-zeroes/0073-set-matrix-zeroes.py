class Solution:
    def mark_infinity(self,matrix,row,col):
        rows = len(matrix)
        cols = len(matrix[0])

        for i in range(rows):
            if matrix[i][col] != 0:
                matrix[i][col] = float("inf")
        
        for j in range(cols):
            if matrix[row][j] != 0:
                matrix[row][j] = float("inf")
    def setZeroes(self, matrix)->None:

        row = len(matrix)
        col = len(matrix[0])

        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j] == 0:
                    self.mark_infinity(matrix,i,j)

        for i in range(0,row):
            for j in range(0,col):
                if matrix[i][j] == float("inf"):
                    matrix[i][j] = 0
        
        


        