# 🧩 Problem: Quick Sort on Key-Value Pairs
#
# 🤔 Difficulty: Medium
#
# 🔗 Link:
#
#     Implement Quick Sort.
#
#     Quick Sort is a divide-and-conquer sorting algorithm that works by partitioning
#     an array into two smaller sub-arrays based on a pivot element.
#     Elements less than the pivot go to the left, and elements greater than or equal
#     go to the right. Then the algorithm recursively sorts the sub-arrays.
#
#     Objective:
#         Given a list of key-value pairs, sort the list by key using Quick Sort.
#
#     Rules:
#         - Use the right-most element as the pivot.
#         - Elements < pivot go left.
#         - Elements >= pivot go right.
#         - Stability is not required.
#
#     Input:
#         - pairs: A list of key-value pairs (int, str), 0 <= len(pairs) <= 100
#
#     Example 1:
#         Input:  [(3, "cat"), (2, "dog"), (3, "bird")]
#         Output: [(2, "dog"), (3, "bird"), (3, "cat")]
#
#     Example 2:
#         Input: [(5, "apple"), (9, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]
#         Output: [(1, "date"), (5, "apple"), (9, "elderberry"), (9, "cherry"), (9, "banana")]
#
# ✅ Constraints:
#     - 0 <= pairs.length <= 100
#     - Each pair is a (key: int, value: str)

from typing import List, Tuple


def quick_sort(pairs: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    """
    Sort a list of (key, value) pairs using quick sort by key.

    Args:
        pairs: A list of (int, str) tuples

    Returns:
        A new list sorted by key
    """
    # Your solution here
    n = len(pairs)
    start = 0
    end = n - 1
    qs_helper(array=pairs, start=start, end=end)

    return pairs


def qs_helper(
    array: List[Tuple[int, str]], start: int, end: int
) -> list[tuple[int, str]] | None:
    # base case

    if end - start + 1 <= 1:
        return array

    # Get the pivot
    pivot = array[end]

    # Init a pointer to keep track of the write pos (it starts at start)
    W = start

    # Loop over the array from start up to end (exclusive since we won't touch pivot)
    for i in range(start, end):
        if array[i][0] < pivot[0]:
            tmp = array[i]
            array[i] = array[W]
            array[W] = tmp
            W += 1  # Advance the write pointer

    # Swap the elem at W with the pivot
    array[end] = array[W]
    array[W] = pivot

    # Recursively sort the left and right splits (excluding the pivot)
    qs_helper(array=array, start=start, end=W - 1)
    qs_helper(array=array, start=W + 1, end=end)


# ✅ Test suite
def test_quick_sort():
    # Since stability is not required, we'll check sorted output by keys only
    def keys_only(pairs: List[Tuple[int, str]]) -> List[int]:
        return [k for k, _ in pairs]

    test_cases = [
        (
            [(3, "cat"), (2, "dog"), (3, "bird")],
            [2, 3, 3],
        ),
        (
            [
                (5, "apple"),
                (9, "banana"),
                (9, "cherry"),
                (1, "date"),
                (9, "elderberry"),
            ],
            [1, 5, 9, 9, 9],
        ),
        (
            [],
            [],
        ),
        (
            [(1, "a")],
            [1],
        ),
        (
            [(4, "z"), (3, "y"), (2, "x"), (1, "w")],
            [1, 2, 3, 4],
        ),
        (
            [(5, "a"), (1, "b"), (3, "c"), (1, "d"), (4, "e")],
            [1, 1, 3, 4, 5],
        ),
    ]

    for i, (input_pairs, expected_sorted_keys) in enumerate(test_cases):
        result = quick_sort(input_pairs)
        result_keys = keys_only(result)
        assert result_keys == expected_sorted_keys, (
            f"Test case {i} failed.\nExpected keys: {expected_sorted_keys}\nGot: {result_keys}"
        )

    print("✅ All test cases passed for quick sort!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing quick sort implementation")
    test_quick_sort()
