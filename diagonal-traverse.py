"""
Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105


https://leetcode.com/problems/diagonal-traverse
"""

import collections
from typing import List
class Solution:
    def findDiagonalOrder(self, grid: List[List[int]]) -> List[int]:
        rows = len(grid)
        cols = len(grid[0])

        d = collections.defaultdict(list)

        for r in range(rows):
            for c in range(cols):
                d[r+c].append(grid[r][c])

        ans = []

        big_sum = rows + cols -1

        for i in range(big_sum):
            if i in d:
                if i % 2 == 0:
                    ans.extend(d[i][::-1])
                else:
                    ans.extend(d[i])
        
        return ans
