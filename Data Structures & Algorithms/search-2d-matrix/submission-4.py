class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # O(log (MN) = O(logm) + O(log(N)
        rows = len(matrix)
        cols = len(matrix[0])

        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        # lets find which row 
        top = 0 
        bottom = rows-1 # 1 

        t_row = (top + bottom)//2

        while top <= bottom:
            mid = (top + bottom)//2
            if matrix[mid][0] > target:
                bottom = mid -1 
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                t_row = mid
                break

        left = 0 
        right = cols-1 

        while left <= right:
            mid = (left+ right)//2
            if target == matrix[t_row][mid]:
                return True
            elif target > matrix[t_row][mid]:
                left = mid + 1
            else:
                right = mid -1 

        return False


