# 🧩 Problem: Bucket Sort
#
# 🤔 Difficulty: Medium
#
# 🔗 Link:
#
#     Implement Bucket Sort.
#
#     Bucket Sort is a sorting algorithm that distributes elements into several buckets.
#     Each bucket is then sorted individually (often using another sorting algorithm),
#     and the results are concatenated to form the final sorted array.
#
#     Objective:
#         Given a list of float values in the range [0, 1), sort the list in ascending order.
#
#     Input:
#         - values: A list of float numbers such that 0 <= value < 1
#
#     Output:
#         - A sorted list of floats
#
#     Example 1:
#         Input:  [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
#         Output: [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94]
#
# ✅ Constraints:
#     - 0 <= len(values) <= 1000
#     - All values are floats in the range [0, 1)

from typing import List


def bucket_sort(values: List[float]) -> List[float]:
    """
    Sort a list of floats in the range [0, 1) using bucket sort.

    Args:
        values: List of float numbers

    Returns:
        A new list sorted in ascending order
    """
    # Your solution here
    n = len(values)

    buckets = [[] for _ in range(n)]

    for num in values:
        idx = int(num * n)
        buckets[idx].append(num)

    # Sort the actual values in the buckets
    for bucket in buckets:
        bucket.sort()

    L = 0
    for i in range(n):
        for j in range(len(buckets[i])):
            values[L] = buckets[i][j]
            L += 1

    return values


# ✅ Test suite
def test_bucket_sort():
    test_cases = [
        (
            [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68],
            [0.12, 0.17, 0.21, 0.23, 0.26, 0.39, 0.68, 0.72, 0.78, 0.94],
        ),
        (
            [],
            [],
        ),
        (
            [0.3],
            [0.3],
        ),
        (
            [0.9, 0.8, 0.7, 0.6],
            [0.6, 0.7, 0.8, 0.9],
        ),
        (
            [0.1, 0.4, 0.3, 0.2, 0.0],
            [0.0, 0.1, 0.2, 0.3, 0.4],
        ),
        (
            [0.999, 0.998, 0.997],
            [0.997, 0.998, 0.999],
        ),
    ]

    for i, (input_vals, expected_sorted) in enumerate(test_cases):
        result = bucket_sort(input_vals)
        assert result == expected_sorted, (
            f"Test case {i} failed.\nInput: {input_vals}\nExpected: {expected_sorted}\nGot: {result}"
        )

    print("✅ All test cases passed for bucket sort!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing bucket sort implementation")
    test_bucket_sort()
