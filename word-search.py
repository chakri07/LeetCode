'''
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Link:https://leetcode.com/problems/word-search/
'''

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """
            If the first letter of the word is found, perform a DFS 
        """
        length = len(word)
        nr_row = len(board)
        nr_col = len(board[0])
        
        
        def dfs(row, col, index):
            if index == length:
                return True
            
            if row < 0 or col < 0 or row>= nr_row or col >= nr_col or board[row][col] != word[index]:
                return False
            
            value = board[row][col]
            board[row][col] = "#" # mark as visited so that we don't visit it again
            
            result = (dfs(row, col + 1, index + 1) or \
                        dfs(row + 1, col, index + 1) or \
                            dfs(row -1, col, index + 1) or \
                                dfs(row, col -1, index + 1))
            
            board[row][col] = value
            
            return result
            
        
        
        for i in range(nr_row):
            for j in range(nr_col):
                if dfs(i, j, 0):
                    return True
             
        return False