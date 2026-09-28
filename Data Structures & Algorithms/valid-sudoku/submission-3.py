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

        for sq in range(9):
            sqrs = set()
            for i in range(3):
                for j in range(3):
                    row = (sq // 3) * 3 + i
                    col = (sq % 3) * 3 + j
                    if board[row][col] != '.':
                        if board[row][col] in sqrs:
                            return False
                        sqrs.add(board[row][col])
                        col += 1

        return True



    #i, j = 0; sq = 3; 0 3 =  3 -> (sq // 3) * 3                                         row = 3