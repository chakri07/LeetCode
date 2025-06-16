"""

Assume the following rules are for the tic-tac-toe game on an n x n board between two players:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves are allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game.
Implement the TicTacToe class:

TicTacToe(int n) Initializes the object the size of the board n.
int move(int row, int col, int player) Indicates that the player with id player plays at the cell (row, col) of the board. The move is guaranteed to be a valid move, and the two players alternate in making moves. Return
0 if there is no winner after the move,
1 if player 1 is the winner after the move, or
2 if player 2 is the winner after the move.

https://leetcode.com/problems/design-tic-tac-toe
"""

class TicTacToe:

    def __init__(self, n: int):
        self.rows = [0] * n 
        self.cols = [0] * n 
        self.diagonal = 0
        self.anti_diagonal = 0
        self.n = n
    def move(self, row: int, col: int, player: int) -> int:
        if player == 1:
            val = 1
        else:
            val = -1
        
        self.rows[row] += val
        self.cols[col] += val

        if (row == col):
            self.diagonal += val
        
        if row + col == self.n-1:
            self.anti_diagonal += val
        n = self.n
        if abs(self.rows[row]) == n or abs(self.cols[col]) == n or \
              abs(self.diagonal) == n or abs(self.anti_diagonal) == n:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)