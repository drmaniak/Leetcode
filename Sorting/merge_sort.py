# 🧩 Problem: Merge Sort on Key-Value Pairs
#
#     Implement Merge Sort.
#
#     Merge Sort is a divide-and-conquer algorithm for sorting an array or list of elements.
#     It works by recursively dividing the unsorted list into n sub-lists, each containing one element.
#     Then, it repeatedly merges sub-lists to produce new sorted sub-lists until one sorted list remains.
#
#     Objective:
#         Given a list of key-value pairs, sort the list by key using Merge Sort.
#         Maintain stability: if two elements have the same key, their relative order must be preserved.
#
#     Input:
#         - pairs: A list of key-value pairs (int, str), with 0 <= pairs.length <= 100
#
#     Example 1:
#         Input:  [(5, "apple"), (2, "banana"), (9, "cherry"), (1, "date"), (9, "elderberry")]
#         Output: [(1, "date"), (2, "banana"), (5, "apple"), (9, "cherry"), (9, "elderberry")]
#
#     Example 2:
#         Input: [(3, "cat"), (2, "dog"), (3, "bird")]
#         Output: [(2, "dog"), (3, "cat"), (3, "bird")]
#
# ✅ Constraints:
#     - 0 <= pairs.length <= 100
#     - Each pair is a (key: int, value: str)

from typing import List, Tuple


def merge_sort(pairs: List[Tuple[int, str]]) -> List[Tuple[int, str]]:
    """
    Sort a list of (key, value) pairs using stable merge sort by key.

    Args:
        pairs: A list of (int, str) tuples

    Returns:
        A new list sorted by key with original order preserved for equal keys
    """
    # Your solution here

    # Edge case
    if not pairs:
        return []

    n = len(pairs)

    # Base case for recursion
    if n == 1:
        return pairs

    # Find midpoint to split the list
    mid = n // 2

    # Recursive call to split lists further
    left_part = merge_sort(pairs[:mid])
    right_part = merge_sort(pairs[mid:])

    merged_list = merge_lists(left_part, right_part)

    return merged_list


def merge_lists(
    left: List[Tuple[int, str]], right: List[Tuple[int, str]]
) -> List[Tuple[int, str]]:
    nl, nr = len(left), len(right)
    out = []

    # Pointers for the left/right lists
    L = 0
    R = 0

    while (L < nl) and (R < nr):
        numL = left[L][0]
        numR = right[R][0]

        if numL <= numR:
            out.append(left[L])
            L += 1
        else:
            out.append(right[R])
            R += 1

    if L == nl:
        out.extend(right[R:])
    else:
        out.extend(left[L:])

    return out


# ✅ Test suite
def test_merge_sort():
    test_cases = [
        (
            [
                (5, "apple"),
                (2, "banana"),
                (9, "cherry"),
                (1, "date"),
                (9, "elderberry"),
            ],
            [
                (1, "date"),
                (2, "banana"),
                (5, "apple"),
                (9, "cherry"),
                (9, "elderberry"),
            ],
        ),
        (
            [(3, "cat"), (2, "dog"), (3, "bird")],
            [(2, "dog"), (3, "cat"), (3, "bird")],
        ),
        (
            [],
            [],
        ),
        (
            [(4, "x")],
            [(4, "x")],
        ),
        (
            [(4, "a"), (1, "b"), (3, "c"), (2, "d")],
            [(1, "b"), (2, "d"), (3, "c"), (4, "a")],
        ),
        (
            [(1, "a"), (1, "b"), (1, "c")],
            [(1, "a"), (1, "b"), (1, "c")],  # should preserve order
        ),
    ]

    for i, (input_pairs, expected_sorted) in enumerate(test_cases):
        result = merge_sort(input_pairs)
        assert result == expected_sorted, (
            f"Test case {i} failed.\nExpected: {expected_sorted}\nGot: {result}"
        )

    print("✅ All test cases passed for merge sort!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing merge sort implementation")
    test_merge_sort()
