class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])        

        def helper(board, word, visited,row,col):
            if not word:
                return True
            
            if row >= rows or row < 0 or \
                col >= cols or col < 0 or \
                visited[row][col] or board[row][col] != word[0]:
                return False 

            visited[row][col] = True
            found = False
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                found |= helper(board, word[1:], visited, row + dr, col + dc)
            visited[row][col] = False  # Backtrack
            return found
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited = [[False for _ in range(cols)] for _ in range(rows)]
                    if helper(board,word,visited,i,j):
                        return True
        
        return False

        







