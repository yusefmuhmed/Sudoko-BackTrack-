import time


class SolveSudoku:

    def find_empty(self, puzzel):

        for r in range(9):
            for c in range(9):
                if puzzel[r][c] == -1:
                    return r, c

        return None, None  # if no spaces

    def validity(self, puzzel, guess, row, col):

        row_val = puzzel[row]  # check in row
        if guess in row_val:
            return False

        col_val = [puzzel[i][col] for i in range(9)]  # check in col
        if guess in col_val:
            return False

        box_row = (row // 3) * 3  # check in box 3*3
        box_col = (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if puzzel[r][c] == guess:
                    return False
        return True

    def solve_sudoku(self, puzzel):

        row, col = self.find_empty(puzzel)
        if row is None:
            return True

        for guess in range(1, 10):
            if self.validity(puzzel, guess, row, col):
                puzzel[row][col] = guess
                if self.solve_sudoku(puzzel):
                    return True
            puzzel[row][col] = -1
        return False


if __name__ == '__main__':
    start = time.time()
    obj = SolveSudoku()

    board = [
        [7, 2, -1, 5, -1, -1, -1, -1, -1],

        [5, -1, -1, -1, 4, -1, 6, -1, -1],

        [-1, 8, -1, 1, -1, -1, -1, -1, -1],

        [-1, -1, -1, -1, -1, 3, -1, -1, 9],

        [-1, 4, 3, -1, -1, -1, -1, -1, -1],

        [-1, -1, -1, -1, -1, 6, -1, 5, -1],

        [-1, -1, 1, 6, -1, -1, 4, -1, 7],

        [-1, -1, -1, -1, -1, 9, -1, -1, -1],

        [-1, 9, -1, -1, -1, -1, -1, 2, -1]
    ]
    print(obj.solve_sudoku(board))
    print(board)
end = time.time()
print(f"Runtime of the program is {end - start}")
