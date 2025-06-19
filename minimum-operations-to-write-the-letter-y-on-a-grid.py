"""

You are given a 0-indexed n x n grid where n is odd, and grid[r][c] is 0, 1, or 2.

We say that a cell belongs to the Letter Y if it belongs to one of the following:

The diagonal starting at the top-left cell and ending at the center cell of the grid.
The diagonal starting at the top-right cell and ending at the center cell of the grid.
The vertical line starting at the center cell and ending at the bottom border of the grid.
The Letter Y is written on the grid if and only if:

All values at cells belonging to the Y are equal.
All values at cells not belonging to the Y are equal.
The values at cells belonging to the Y are different from the values at cells not belonging to the Y.
Return the minimum number of operations needed to write the letter Y on the grid given that in one operation you can change the value at any cell to 0, 1, or 2.

 

Example 1:


Input: grid = [[1,2,2],[1,1,0],[0,1,0]]
Output: 3
Explanation: We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 1 while those that do not belong to Y are equal to 0.
It can be shown that 3 is the minimum number of operations needed to write Y on the grid.
Example 2:


Input: grid = [[0,1,0,1,0],[2,1,0,1,2],[2,2,2,0,1],[2,2,2,2,2],[2,1,2,2,2]]
Output: 12
Explanation: We can write Y on the grid by applying the changes highlighted in blue in the image above. After the operations, all cells that belong to Y, denoted in bold, have the same value of 0 while those that do not belong to Y are equal to 2. 
It can be shown that 12 is the minimum number of operations needed to write Y on the grid.


https://leetcode.com/problems/minimum-operations-to-write-the-letter-y-on-a-grid
"""

from collections import defaultdict
from typing import List

class Solution:
    def minimumOperationsToWriteY(self, grid: List[List[int]]) -> int:
        y_counts = defaultdict(int)
        rest = defaultdict(int)

        rows = len(grid)
        cols = len(grid[0])

        mid = rows//2
        
        for r in range(rows):
            for c in range(cols):

                # if the cell in y 1st slant 
                if r == c and r < mid:
                    y_counts[grid[r][c]] += 1
                elif r + c == cols -1 and r < mid:
                    y_counts[grid[r][c]] += 1
                elif c == cols//2 and r >= mid:
                    y_counts[grid[r][c]] += 1
                else:
                   rest[grid[r][c]] += 1
        

        ans = float('inf')
        y_num = 0 
        for val, count in y_counts.items():
            y_num += count

        rest_num = (rows * rows) - y_num

        for rest_val in range(3):
            for y_val in range(3):
                if y_val == rest_val:
                    continue
                rest_operations = rest_num - rest[rest_val]
                y_opeartions = y_num - y_counts[y_val]

                ans = min(ans, rest_operations + y_opeartions)

        return ans
