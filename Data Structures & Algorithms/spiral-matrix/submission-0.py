class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        rows = len(matrix)
        cols = len(matrix[0])

        left = 0 
        right = cols-1
        up = 0
        down = rows-1 

        result = []

        while len(result) < (rows * cols):
            #traverse left to right
            for col in range(left, right+1):
                result.append(matrix[up][col])
            up += 1
            

            # Traverse up to down
            
            for row in range(up, down+1):
                result.append(matrix[row][right])
            right -=1


            #Travese right to left
            if up <= down:
                for col in range(right, left-1,-1):
                    result.append(matrix[down][col])
                down -=1 
            
            if left <= right:
                for row in range(down, up-1,-1):
                    result.append(matrix[row][left])
                left +=1

        return result
