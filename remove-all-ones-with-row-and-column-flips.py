'''
You are given an m x n binary matrix grid.

In one operation, you can choose any row or column and flip each value in that row or column (i.e., changing all 0's to 1's, and all 1's to 0's).

Return true if it is possible to remove all 1's from grid using any number of operations or false otherwise.

 

Example 1:


Input: grid = [[0,1,0],[1,0,1],[0,1,0]]
Output: true
Explanation: One possible way to remove all 1's from grid is to:
- Flip the middle row
- Flip the middle column

https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/
'''

from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        if len(grid) == 0:
            return False
        
        row1 = grid[0]
        row1_inv = []
        
        for num in row1:
            if num == 1:
                row1_inv.append(0)
            else:
                row1_inv.append(1)
        
        for row in grid:
            if row != row1 and row != row1_inv:
                return False
            
        return True
