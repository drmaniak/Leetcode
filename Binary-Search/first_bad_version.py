# 🧩 Problem: First Bad Version
#
# 🤔 Difficulty: Easy
#
# 🔗 Link: https://leetcode.com/problems/first-bad-version
#
#     You are a product manager and currently leading a team to develop a new product.
#     Unfortunately, the latest version of your product fails the quality check.
#     Since each version is developed based on the previous one, all versions after a bad version are also bad.
#
#     You are given an API `isBadVersion(version)` which returns True if a version is bad.
#     Implement a function to find the first bad version.
#     You should minimize the number of calls to the API.
#
#     Example 1:
#         Input:  n = 5, bad = 4
#         Output: 4
#         Explanation:
#             call isBadVersion(3) -> False
#             call isBadVersion(5) -> True
#             call isBadVersion(4) -> True
#
#     Example 2:
#         Input:  n = 1, bad = 1
#         Output: 1
#
# ✅ Constraints:
#     - 1 <= bad <= n <= 2^31 - 1

from typing import Callable


def first_bad_version(n: int, isBadVersion: Callable[[int], bool]) -> int:
    """
    Find the first bad version among versions 1 to n.

    Args:
        n: Total number of versions
        isBadVersion: API that returns True if a given version is bad

    Returns:
        The version number of the first bad version
    """
    # Your solution here
    low = 1
    high = n

    first = -1

    while low <= high:
        mid = (high + low) // 2

        if isBadVersion(mid):
            first = mid
            high = mid - 1
        elif not isBadVersion(mid):
            low = mid + 1

    return first


# ✅ Test suite
def test_first_bad_version():
    def make_is_bad_version(bad: int) -> Callable[[int], bool]:
        """Factory to create an isBadVersion function with the given first bad version."""

        def is_bad(version: int) -> bool:
            return version >= bad

        return is_bad

    test_cases = [
        (5, 4, 4),
        (1, 1, 1),
        (10, 1, 1),
        (10, 10, 10),
        (100, 73, 73),
        (2, 2, 2),
        (1000000, 999999, 999999),
    ]

    for i, (n, bad, expected) in enumerate(test_cases):
        is_bad = make_is_bad_version(bad)
        result = first_bad_version(n, is_bad)
        assert result == expected, (
            f"Test case {i} failed.\nInput: n={n}, bad={bad}\nExpected: {expected}, Got: {result}"
        )

    print("✅ All test cases passed for first bad version!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing first_bad_version implementation")
    test_first_bad_version()
