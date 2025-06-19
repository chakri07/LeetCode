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
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])

        dirs = [(0,1),(1,0),(-1,0),(0,-1)]


        def dfs(r,c,word,visited):
            if not word:
                return True
            

            for dr,dc in dirs:
                nr, nc = r+dr , c+dc 
                if 0 <= nr < rows and 0 <= nc < cols:
                    if (nr, nc) not in visited and board[nr][nc] == word[0]:
                        visited.add((nr,nc))
                        if dfs(nr, nc, word[1:],visited):
                            return True
                        visited.remove((nr,nc))

            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    visited = set()
                    visited.add((r,c))
                    if dfs(r,c, word[1:], visited):
                        return True 

        return False    


# Backtracking DFS
# Dont forget to remove the element which is not part of the word.

from collections import deque
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,word,visited):
            if len(word) == 1:
                if board[r][c] == word[0]:
                    return True
                else:
                    return False

            if not board[r][c] == word[0]:
                return False

            visited.add((r,c))
            
            neighbours = [(1,0),(0,1),(-1,0),(0,-1)]

            for dr,dc in neighbours:
                nr,nc = r+dr,c+dc

                if 0 <= nr < rows and 0 <= nc < cols \
                    and (nr,nc) not in visited:
                        if dfs(nr,nc,word[1:],visited):
                            return True
            # Dont forget this step 
            # if this is false this can be part of the word later 
            # so we should mark it as non visited
            # if true we dont need to do this since 
            # the letter is in the word and should n't be visited again
            visited.remove((r,c))
            
            return False

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,word,set()):
                    return True
        
        return False


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

# Backtracking solution 
from typing import List
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
