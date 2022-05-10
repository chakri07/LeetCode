'''
Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

 

Example 1:


Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
Example 2:

Input: board = [["X"]]
Output: [["X"]]

Link:https://leetcode.com/problems/surrounded-regions/
'''


class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        if m <=2 or n <=2:
            return board
        # now let's assume m>=3 and n>=3
        from collections import deque
        
        queue = deque([])
        
        def valid(x, y):
            return x>=0 and x<=m-1 and y>=0 and y<=n-1
        
        for i in range(0, m):
            if board[i][0] == "O":
                queue.append((i, 0))
            if board[i][n-1] == "O":
                queue.append((i, n-1))
        for j in range(0, n):
            if board[0][j] == "O":
                queue.append((0, j))
            if board[m-1][j] == "O":
                queue.append((m-1, j))
                
        while queue:
            x, y = queue.popleft()
            if board[x][y] == "O": # not captured yet
                board[x][y] = "N"
                if valid(x+1, y) and board[x+1][y] == "O":
                    queue.append((x+1, y))
                if valid(x-1, y) and board[x-1][y] == "O":
                    queue.append((x-1, y))
                if valid(x, y+1) and board[x][y+1] == "O":
                    queue.append((x, y+1))
                if valid(x, y-1) and board[x][y-1] == "O":
                    queue.append((x, y-1))
                    
            else: # board[x][y] == "X" or "N"
                pass
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "N":
                    board[i][j] = "O"
        return board
        
        