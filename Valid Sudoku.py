class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean

            
    def checkRow(self , board):
        r = 9
        rh = [{} for i in range(r)]
        ch = [{} for i in range(r)]
        for i in range(r):
            for j in range(r):
                if board[i][j] != '.':
                    if board[i][j] in rh[j] or board[i][j] in ch[i]:
                        return False
                    ch[i][ board[i][j] ] = 1
                    rh[j][ board[i][j] ] = 1
        return True
    def checkBox(self , board):
        for i in range(0 , 7 , 3):
            for j in range(0 , 7 , 3):
                h = {}
                for k in range(i , i + 3):
                    for e in range(j , j + 3):
                        if board[k][e] != '.' and board[k][e] in h:
                            return False
                        h[ board[k][e] ] = 1
        return True
    def isValidSudoku(self, board):
        return self.checkRow(board) and self.checkBox(board)
        