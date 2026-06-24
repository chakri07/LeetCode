class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row_set = set()
        col_set = set()

        rows = len(matrix)
        cols = len(matrix[0])
        
        for r in range(0,rows):
            for c in range(0,cols):
                if matrix[r][c] == 0:
                    row_set.add(r)
                    col_set.add(c)  

        for r in range(0,rows):
            for c in range(0,cols):
                if (r in row_set) or (c in col_set):
                    matrix[r][c] = 0


        

        