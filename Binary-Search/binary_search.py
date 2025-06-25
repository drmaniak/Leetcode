# 🧩 Problem: Binary Search
#
#     You are given an array of distinct integers `nums`, sorted in ascending order,
#     and an integer `target`.
#
#     Implement a function to search for `target` within `nums`. If it exists,
#     return its index. Otherwise, return -1.
#
#     Your solution must run in O(log n) time.
#
#     Example 1:
#         Input:  nums = [-1, 0, 2, 4, 6, 8], target = 4
#         Output: 3
#
#     Example 2:
#         Input:  nums = [-1, 0, 2, 4, 6, 8], target = 3
#         Output: -1
#
# ✅ Constraints:
#     - 1 <= nums.length <= 10,000
#     - -10,000 < nums[i], target < 10,000
#     - All integers in nums are unique
#     - nums is sorted in strictly increasing order

from typing import List


def binary_search(nums: List[int], target: int) -> int:
    """
    Perform binary search to find target in sorted list of unique integers.

    Args:
        nums: A list of distinct integers sorted in ascending order
        target: The integer to search for

    Returns:
        The index of target if found, otherwise -1
    """
    # Your solution here

    n = len(nums)

    L, R = 0, n - 1

    while L <= R:
        mp = (L + R) // 2
        mtarget = nums[mp]

        if target < mtarget:
            R = mp - 1
        elif target > mtarget:
            L = mp + 1
        else:
            return mp

    return -1


# ✅ Test suite
def test_binary_search():
    test_cases = [
        ([-1, 0, 2, 4, 6, 8], 4, 3),
        ([-1, 0, 2, 4, 6, 8], 3, -1),
        ([1], 1, 0),
        ([1], 0, -1),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 3, 2),
        ([-10, -5, 0, 3, 7, 12], 12, 5),
        ([-10, -5, 0, 3, 7, 12], -10, 0),
        ([-10, -5, 0, 3, 7, 12], -4, -1),
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        result = binary_search(nums, target)
        assert result == expected, (
            f"Test case {i} failed.\nInput: nums={nums}, target={target}\nExpected: {expected}, Got: {result}"
        )

    print("✅ All test cases passed for binary search!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing binary search implementation")
    test_binary_search()
