class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        
        
        for i in range(9):
            cols = []
            for j in range(9):
                if board[j][i] != '.':
                    cols.append(int(board[j][i]))
            if len(cols)!=len(set(cols)):
                return False

        for i in range(9):
            rows = []
            for j in range(9):
                if board[i][j] != '.':
                    rows.append(int(board[i][j]))
            if len(rows)!=len(set(rows)):
                return False
        
        for i in range(0,9,3):
            for j in range(0,9,3):
                boxes = []
                for i2 in range(i, i+3):
                    for j2 in range(j, j+3):
                        if board[i2][j2] != '.':
                            boxes.append(int(board[i2][j2]))
                if len(boxes)!=len(set(boxes)):
                    return False
        return True
            
