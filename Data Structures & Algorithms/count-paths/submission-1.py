class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[ 0 for _ in range(n)] for _ in range(m)]

        grid[0][0] = 1
        for i in range(m):
            grid[i][0] = 1
        for i in range(n):
            grid[0][i] = 1

        for row in range(1,m):
            for col in range(1,n):
                cell_val = 0 
                if row -1 >= 0:
                    cell_val = cell_val + grid[row -1][col]
                if col-1 >= 0:
                    cell_val = cell_val + grid[row][col-1]

                grid[row][col] = cell_val

        return grid[m-1][n-1]
