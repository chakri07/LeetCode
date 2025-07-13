"""

Given an m x n matrix, return all elements of the matrix in spiral order.



https://leetcode.com/problems/spiral-matrix
"""

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        up = 0 
        left = 0 
        right = cols - 1
        down = rows - 1

        while len(result) < rows * cols:
            # Traverse from left to right
            for col in range(left, right+1):
                result.append(matrix[up][col])
            
            # traverse downward
            for row in range(up +1, down+1):
                result.append(matrix[row][right])

            # traverse right to left 
            if up != down:
                for col in range(right-1,left-1, -1):
                    result.append(matrix[down][col])
            
            # traverse upward
            if left != right:
                for row in range(down-1,up, -1):
                    result.append(matrix[row][left])

            left += 1
            up += 1
            down -= 1
            right -=1

        return result

from typing import List
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        results = []
        rows = len(matrix)
        cols = len(matrix[0])

        up = 0 
        left = 0 
        right = cols - 1
        down = rows - 1

        while len(results) < (rows * cols):
            # left to right
            for col in range(left, right+1):
                results.append(matrix[up][col])
            up += 1
            # then top to down
            for row in range(up, down+1):
                results.append(matrix[row][right])
            
            right -= 1
            # then right to left
            if up <= down:
                for col in range(right, left-1, -1):
                    results.append(matrix[down][col])
                down -= 1 
                
            # down to up
            if left <= right:
                for row in range(down, up -1,-1):
                    results.append(matrix[row][left])
                left += 1

        return results
