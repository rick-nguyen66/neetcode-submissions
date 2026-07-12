class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # check entire row (i)
        # check entire col (j)
        # check 3x3 (0-2, 3-5, 6-8)

        for row in range(9):
            s = set()
            for i in range(9):
                if board[row][i] == '.':
                    continue
                if board[row][i] in s:
                    return False
                s.add(board[row][i])

        for col in range(9):
            s = set()
            for i in range(9):
                if board[i][col] == '.':
                    continue
                if board[i][col] in s:
                    return False
                s.add(board[i][col])

        for square in range(9):
            s = set()
            for i in range(3):
                for j in range(3):
                    row = (square // 3) * 3 + i
                    col = (square % 3) * 3 + j
                    curr = board[row][col]
                    if curr == '.':
                        continue
                    if curr in s:
                        return False
                    s.add(curr)

        return True