# 🧩 Problem: Search a 2D Matrix
#
# 🤔 Difficulty: Medium
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

    # Get count of rows and cols
    rows, cols = len(matrix), len(matrix[0])

    # We need to first perform binary search top-to-bottom to find correct row
    TOP = 0
    BOTTOM = rows - 1

    vert_mid = 0

    while TOP <= BOTTOM:
        vert_mid = (TOP + BOTTOM) // 2

        vert_target_lower = matrix[vert_mid][0]
        vert_target_upper = matrix[vert_mid][-1]

        if target < vert_target_lower:
            BOTTOM = vert_mid - 1
        elif target > vert_target_upper:
            TOP = vert_mid + 1
        else:
            break

    if not (TOP <= BOTTOM):
        return False

    LEFT = 0
    RIGHT = cols - 1
    while LEFT <= RIGHT:
        hori_mid = (LEFT + RIGHT) // 2

        hori_target = matrix[vert_mid][hori_mid]

        if target < hori_target:
            RIGHT = hori_mid - 1
        elif target > hori_target:
            LEFT = hori_mid + 1
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
