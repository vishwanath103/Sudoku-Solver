def find_next_empty(puzzle):
    # return row,col tuple (or (None,None) if there is no empty square)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c

    return None, None

def is_valid(puzzle, guess, row, col):
    # returns True if it is valid, False otherwise

    # check in the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    # Check in the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    # Check the square
    row_start = (row//3)*3
    col_start = (col//3)*3
    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    # solve sudoku using backtracking

    # step 1: Choose somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    # step 2: if there is a place to put a number, then make a guess
    for guess in range(1,10):
        # step 3: check if this is a valid guess or not
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # recursively solve sudoku using this puzzle state
            if solve_sudoku(puzzle):
                return True

        # In case of non-valid guess number
        puzzle[row][col] = -1 # reset helps in backtracking

    return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
