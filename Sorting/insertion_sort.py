# 🧩 Problem: Insertion Sort on Key-Value Pairs
#
# 🤔 Difficulty: Medium
#
# 🔗 Link:
#
#     Implement Insertion Sort and return intermediate states.
#
#     Insertion Sort is a simple sorting algorithm that builds the sorted list one element
#     at a time from left to right. It works by repeatedly taking an element from the
#     unsorted portion and inserting it into its correct position in the sorted portion.
#
#     Objective:
#         Given a list of key-value pairs, sort the list by key using Insertion Sort.
#         Return a list of lists showing the state of the array after each insertion.
#
#     ⚠️ If two key-value pairs have the same key, maintain their relative order
#     (i.e., your sort must be stable).
#
#     Input:
#         - pairs: A list of key-value pairs (int, str), with 0 <= pairs.length <= 100
#
#     Example 1:
#         Input:  [(5, "apple"), (2, "banana"), (9, "cherry")]
#         Output: [[(5, "apple"), (2, "banana"), (9, "cherry")],
#                  [(2, "banana"), (5, "apple"), (9, "cherry")],
#                  [(2, "banana"), (5, "apple"), (9, "cherry")]]
#
#     Example 2:
#         Input: [(3, "cat"), (3, "bird"), (2, "dog")]
#         Output: [[(3, "cat"), (3, "bird"), (2, "dog")],
#                  [(3, "cat"), (3, "bird"), (2, "dog")],
#                  [(2, "dog"), (3, "cat"), (3, "bird")]]
#
# ✅ Constraints:
#     - 0 <= pairs.length <= 100
#     - Each pair is a (key: int, value: str)

from typing import List, Tuple


def insertion_sort_states(pairs: List[Tuple[int, str]]) -> List[List[Tuple[int, str]]]:
    """
    Perform insertion sort on a list of (key, value) pairs and return the state of
    the array after each insertion step.

    Args:
        pairs: A list of (int, str) tuples to sort by key.

    Returns:
        A list of array states representing the list after each insertion step.
    """
    # Your solution here

    out = []

    n = len(pairs)

    if not pairs:
        return out

    if len(pairs) == 1:
        return [pairs.copy()]

    out.append(pairs.copy())

    for i in range(1, n):
        N = i
        P = i - 1
        while P >= 0 and (pairs[N][0] < pairs[P][0]):
            tmp = pairs[P]
            pairs[P] = pairs[N]
            pairs[N] = tmp

            N -= 1
            P -= 1

        out.append(pairs.copy())

    return out


# ✅ Test suite
def test_insertion_sort_states():
    test_cases = [
        (
            [(5, "apple"), (2, "banana"), (9, "cherry")],
            [
                [(5, "apple"), (2, "banana"), (9, "cherry")],
                [(2, "banana"), (5, "apple"), (9, "cherry")],
                [(2, "banana"), (5, "apple"), (9, "cherry")],
            ],
        ),
        (
            [(3, "cat"), (3, "bird"), (2, "dog")],
            [
                [(3, "cat"), (3, "bird"), (2, "dog")],
                [(3, "cat"), (3, "bird"), (2, "dog")],
                [(2, "dog"), (3, "cat"), (3, "bird")],
            ],
        ),
        ([], []),
        ([(1, "a")], [[(1, "a")]]),
        (
            [(4, "x"), (3, "y"), (2, "z"), (1, "w")],
            [
                [(4, "x"), (3, "y"), (2, "z"), (1, "w")],
                [(3, "y"), (4, "x"), (2, "z"), (1, "w")],
                [(2, "z"), (3, "y"), (4, "x"), (1, "w")],
                [(1, "w"), (2, "z"), (3, "y"), (4, "x")],
            ],
        ),
    ]

    for i, (input_pairs, expected_states) in enumerate(test_cases):
        result = insertion_sort_states(input_pairs)
        assert result == expected_states, (
            f"Test case {i} failed.\nExpected: {expected_states}\nGot: {result}"
        )

    print("✅ All test cases passed for insertion sort states!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing insertion sort implementation with state tracking")
    test_insertion_sort_states()
