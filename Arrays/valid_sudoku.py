# 🧩 Problem: Valid Sudoku
#
# 🤔 Difficulty: Medium
#
#     Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated
#     according to the following rules:
#
#     1. Each row must contain the digits 1-9 without repetition.
#     2. Each column must contain the digits 1-9 without repetition.
#     3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
#     Note:
#     - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#     - Only the filled cells need to be validated according to the mentioned rules.
#     - The board is represented as a 9x9 2D array of characters where '.' represents empty cells.

# ✅ Constraints
#
#     board.length == 9
#     board[i].length == 9
#     board[i][j] is a digit 1-9 or '.'.

from collections import defaultdict


def is_valid_sudoku(board: list[list[str]]) -> bool:
    """
    Determines if a 9x9 Sudoku board is valid according to Sudoku rules.

    Time Complexity: O(1) since the board size is fixed at 9x9
    Space Complexity: O(1) since the sets used are of fixed size
    """

    for row in range(9):
        checker = set()
        for col in range(9):
            val = board[row][col]

            if val == ".":
                continue

            if val in checker:
                return False
            else:
                checker.add(val)

    for col in range(9):
        checker = set()
        for row in range(9):
            val = board[row][col]

            if val == ".":
                continue

            if val in checker:
                return False
            else:
                checker.add(val)

    gridcheck = defaultdict(set)
    for row in range(9):
        for col in range(9):
            gr = row // 3
            gc = col // 3

            val = board[row][col]

            if val == ".":
                continue

            if val in gridcheck[(gr, gc)]:
                return False
            else:
                gridcheck[(gr, gc)].add(val)

    return True


def is_valid_sudoku_optimized(board: list[list[str]]) -> bool:
    """
    Determines if a 9x9 Sudoku board is valid in a single pass.

    Time Complexity: O(1) since the board size is fixed at 9x9
    Space Complexity: O(1) since the sets used are of fixed size
    """

    rowcheck = defaultdict(set)
    colcheck = defaultdict(set)
    gridcheck = defaultdict(set)

    for row in range(9):
        for col in range(9):
            val = board[row][col]

            gr, gc = row // 3, col // 3

            if val == ".":
                continue

            if (
                (val in rowcheck[row])
                or (val in colcheck[col])
                or (val in gridcheck[(gr, gc)])
            ):
                return False
            else:
                rowcheck[row].add(val)
                colcheck[col].add(val)
                gridcheck[(gr, gc)].add(val)

    return True


# ✅ Thorough test suite
def test_is_valid_sudoku(optimized=False):
    # Example 1: Valid Sudoku
    valid_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert is_valid_sudoku(valid_board) == True
    if optimized:
        assert is_valid_sudoku_optimized(valid_board) == True

    # Example 2: Invalid Sudoku - duplicate in row
    invalid_row_board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert is_valid_sudoku(invalid_row_board) == False
    if optimized:
        assert is_valid_sudoku_optimized(invalid_row_board) == False

    # Invalid Sudoku - duplicate in column
    invalid_col_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", "6", "5"],  # Duplicate 6 in column 7
        [".", ".", ".", ".", "8", ".", ".", "3", "9"],
    ]
    assert is_valid_sudoku(invalid_col_board) == False
    if optimized:
        assert is_valid_sudoku_optimized(invalid_col_board) == False

    # Invalid Sudoku - duplicate in 3x3 box
    invalid_box_board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [
            ".",
            ".",
            "8",
            ".",
            "8",
            ".",
            ".",
            "7",
            "9",
        ],  # Duplicate 8 in bottom-center box
    ]
    assert is_valid_sudoku(invalid_box_board) == False
    if optimized:
        assert is_valid_sudoku_optimized(invalid_box_board) == False

    # Empty board (all '.')
    empty_board = [["." for _ in range(9)] for _ in range(9)]
    assert is_valid_sudoku(empty_board) == True
    if optimized:
        assert is_valid_sudoku_optimized(empty_board) == True

    # Board with duplicates in boxes
    invalid_board = [
        [".", ".", ".", ".", "5", ".", ".", "1", "."],
        [".", "4", ".", "3", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "3", ".", ".", "1"],
        ["8", ".", ".", ".", ".", ".", ".", "2", "."],
        [".", ".", "2", ".", "7", ".", ".", ".", "."],
        [".", "1", "5", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", "2", ".", ".", "."],
        [".", "2", ".", "9", ".", ".", ".", ".", "."],
        [".", ".", "4", ".", ".", ".", ".", ".", "."],
    ]
    # This board has duplicates in boxes (Box 1 has two '3's and Box 2 has two '1's)
    assert is_valid_sudoku(invalid_board) == False
    if optimized:
        assert is_valid_sudoku_optimized(invalid_board) == False

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("NORMAL METHOD")
    test_is_valid_sudoku()
    print("#" * 10)
    print("OPTIMIZED METHOD")
    test_is_valid_sudoku(optimized=True)
