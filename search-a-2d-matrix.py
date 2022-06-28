'''
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
 

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

https://leetcode.com/problems/search-a-2d-matrix/
'''

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top = 0 
        bottom = len(matrix)-1
        
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        mid = (top + bottom) //2
        while(top <= bottom): 
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target and matrix[mid][n] >= target:
                print("broke")
                break
            elif matrix[mid][n] < target:
                top = mid + 1
            else:
                bottom = mid - 1
                
        left = 0 
        right = n 
        
        while(left <= right):
            mid2 = (left + right) //2
            if matrix[mid][mid2] == target:
                return True
            elif matrix[mid][mid2] > target:
                right = mid2 - 1
            else:
                left = mid2 + 1
        
        return False
            