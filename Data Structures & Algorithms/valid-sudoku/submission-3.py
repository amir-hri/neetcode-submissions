class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for i in range(n):    
            seen = set()
            for j in range(n):
                val = board[i][j]
                if val=='.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for i in range(n):    
            seen = set()
            for j in range(n):
                val = board[j][i]
                if val=='.':
                    continue
                if val in seen:
                    return False
                seen.add(val)
        for i in range(0, n, 3):
            for j in range(0, n, 3):
                seen = set()
                for r in range(i, i+3):
                    for c in range(j, j+3):
                        val = board[r][c]
                        if val=='.':
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True
