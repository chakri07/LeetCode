class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(r,c,visited):
            neigh = [(1,0),(0,1),(-1,0),(0,-1)]
            visited.add((r,c))
            for dr,dc in neigh:
                nr,nc = r+dr, c+dc
                if 0 <= nr < rows and 0 <= nc < cols \
                     and board[nr][nc] == 'O' and (nr,nc) not in visited:
                    board[nr][nc] = 'T'
                    dfs(nr,nc,visited)
        
        # cols should be constant
        for c in [0,cols-1]:
            for r in range(rows):
                if board[r][c] == 'O':
                    board[r][c] = 'T'
                    dfs(r,c,visited)

        for r in [0,rows-1]:
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'T'
                    dfs(r,c,visited)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] =='O':
                    board[r][c] = 'X'
                elif board[r][c] =='T':
                    board[r][c] = 'O'

