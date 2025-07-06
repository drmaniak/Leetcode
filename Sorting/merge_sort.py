# 🧩 Problem: Merge Sort on Key-Value Pairs
#
# 🤔 Difficulty: Medium
#
# 🔗 Link:
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

    n = len(pairs)

    # Recursive base case
    if n <= 1:
        return pairs

    # What I need to do is to find the midpoint,
    # split the list into left and right parts, and sort the left

    mid = n // 2

    left_part = merge_sort(pairs[:mid])
    right_part = merge_sort(pairs[mid:])

    merged_part = merge_left_right(left_part, right_part)

    return merged_part


def merge_left_right(
    left_part: list[tuple[int, str]], right_part: list[tuple[int, str]]
) -> list[tuple[int, str]]:
    nl, nr = len(left_part), len(right_part)

    out = []

    L, R = 0, 0

    while (L < nl) and (R < nr):
        pair_l = left_part[L]
        pair_r = right_part[R]

        if pair_l[0] <= pair_r[0]:
            out.append(pair_l)
            L += 1
        else:
            out.append(pair_r)
            R += 1

    remainder = left_part[L:] if L != nl else right_part[R:]
    out.extend(remainder)

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
