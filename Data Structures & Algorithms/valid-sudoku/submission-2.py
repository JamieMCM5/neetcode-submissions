class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(9):
            rows = set()
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows:
                        return False
                    rows.add(board[i][j])

        for i in range(9):
            cols = set()
            for j in range(9):
                if board[j][i] != '.':
                    if board[j][i] in cols:
                        return False
                    cols.add(board[j][i])

        for i in range(9):
            sqrs = set()
            for j in range(3):
                for k in range(3):
                    
                    row = (i // 3) * 3 + j
                    col = (i % 3) * 3 + k
                    if board[row][col] != '.':
                        if board[row][col] in sqrs:
                            return False
                        sqrs.add(board[row][col])

        return True
        

