# 🧩 Problem: Search a 2D Matrix
#
# 🤔 Difficulty: Medium
#
# 🔗 Link: https://leetcode.com/problems/search-a-2d-matrix
#
#     You are given an m x n 2D integer array `matrix` and an integer `target`.
#
#     - Each row in `matrix` is sorted in non-decreasing order.
#     - The first integer of each row is greater than the last integer of the previous row.
#
#     Return True if target exists in the matrix, False otherwise.
#
#     You must implement a solution that runs in O(log(m * n)) time.
#
#     Example 1:
#         Input:  matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10
#         Output: True
#
#     Example 2:
#         Input:  matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15
#         Output: False
#
# ✅ Constraints:
#     - m == matrix.length
#     - n == matrix[i].length
#     - 1 <= m, n <= 100
#     - -10,000 <= matrix[i][j], target <= 10,000

from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Search for a target value in a 2D matrix with sorted rows and progressive row starts.

    Args:
        matrix: 2D list of integers
        target: Integer to search for

    Returns:
        True if target exists in matrix, False otherwise
    """

    # Plan: binary search to find correct row -> binary search to find correct column

    # ROW SEARCH
    TOP = 0
    BOTTOM = len(matrix) - 1

    row_mid = 0

    while TOP <= BOTTOM:
        row_mid = (TOP + BOTTOM) // 2
        row_L = matrix[row_mid][0]
        row_R = matrix[row_mid][-1]

        if target < row_L:
            BOTTOM = row_mid - 1
        elif target > row_R:
            TOP = row_mid + 1
        else:
            break

    LEFT = 0
    RIGHT = len(matrix[0]) - 1
    col_mid = 0

    while LEFT <= RIGHT:
        col_mid = (LEFT + RIGHT) // 2
        col_target = matrix[row_mid][col_mid]

        if target < col_target:
            RIGHT = col_mid - 1
        elif target > col_target:
            LEFT = col_mid + 1
        else:
            return True

    return False


# ✅ Test suite
def test_search_matrix():
    test_cases = [
        (
            [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]],
            10,
            True,
        ),
        (
            [[1, 2, 4, 8], [10, 11, 12, 13], [14, 20, 30, 40]],
            15,
            False,
        ),
        (
            [[1]],
            1,
            True,
        ),
        (
            [[1]],
            2,
            False,
        ),
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            3,
            True,
        ),
        (
            [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]],
            13,
            False,
        ),
        (
            [[-10, -5, 0], [2, 4, 6], [8, 10, 15]],
            -5,
            True,
        ),
        (
            [[-10, -5, 0], [2, 4, 6], [8, 10, 15]],
            7,
            False,
        ),
    ]

    for i, (matrix, target, expected) in enumerate(test_cases):
        result = search_matrix(matrix, target)
        assert result == expected, (
            f"Test case {i} failed.\nMatrix: {matrix}\nTarget: {target}\nExpected: {expected}, Got: {result}"
        )

    print("✅ All test cases passed for search 2D matrix!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing search_matrix implementation")
    test_search_matrix()
