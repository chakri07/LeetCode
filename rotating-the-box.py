"""
You are given an m x n matrix of characters boxGrid representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in boxGrid rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.

 

Example 1:



Input: boxGrid = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
Example 2:



Input: boxGrid = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
Example 3:



Input: boxGrid = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
 

Constraints:

m == boxGrid.length
n == boxGrid[i].length
1 <= m, n <= 500
boxGrid[i][j] is either '#', '*', or '.'.

https://leetcode.com/problems/rotating-the-box
"""
from typing import List

class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        new_grid = []

        rows = len(boxGrid)
        cols = len(boxGrid[0])

        for c in range(cols):
            new_grid.append([])
            for r in range(rows-1,-1,-1):
                new_grid[-1].append(boxGrid[r][c])

        # now process each col
        new_rows = len(new_grid)
        new_cols = len(new_grid[0])

        for c in range(new_cols): 
            last_empty= new_rows -1
            for r in range(new_rows-1,-1,-1):
                if new_grid[r][c] == '#':
                    if r != last_empty:
                        new_grid[last_empty][c] = '#'
                        new_grid[r][c] = '.'
                    last_empty -= 1 

                elif new_grid[r][c] == '*':
                    last_empty = r-1

        return new_grid