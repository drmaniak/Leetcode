# 🧩 Problem: Find Minimum in Rotated Sorted Array
#
#     You are given an array of length `n` that was originally sorted in ascending order.
#     It has been rotated between 1 and `n` times.
#
#     For example:
#         [1,2,3,4,5,6] rotated 4 times becomes [3,4,5,6,1,2]
#         [1,2,3,4,5,6] rotated 6 times becomes [1,2,3,4,5,6]
#
#     All elements are unique.
#
#     Return the **minimum element** in the rotated array.
#
#     ⚠️ O(n) solutions are trivial — your goal is to solve it in O(log n) time.
#
#     Example 1:
#         Input:  nums = [3,4,5,6,1,2]
#         Output: 1
#
#     Example 2:
#         Input:  nums = [4,5,0,1,2,3]
#         Output: 0
#
#     Example 3:
#         Input:  nums = [4,5,6,7]
#         Output: 4
#
# ✅ Constraints:
#     - 1 <= nums.length <= 1000
#     - -1000 <= nums[i] <= 1000
#     - All values are unique

from typing import List


def find_min(nums: List[int]) -> int:
    """
    Find the minimum element in a rotated sorted array.

    Args:
        nums: List of unique integers originally sorted, then rotated

    Returns:
        The minimum value in the rotated array
    """
    # Your solution here

    left, right = 0, len(nums) - 1
    res = nums[left]

    while left <= right:
        if nums[left] <= nums[right]:
            res = min(res, nums[left])

        m = (left + right) // 2

        res = min(res, nums[m])
        if nums[m] >= nums[left]:
            left = m + 1
        else:
            right = m - 1

    return res


# ✅ Test suite
def test_find_min():
    test_cases = [
        ([3, 4, 5, 6, 1, 2], 1),
        ([4, 5, 0, 1, 2, 3], 0),
        ([4, 5, 6, 7], 4),
        ([2, 3, 4, 5, 6, 1], 1),
        ([6, 1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5], 1),  # no rotation
        ([2], 2),  # single element
        ([7, 8, 9, 1, 2, 3, 4, 5, 6], 1),
        ([2, 3, 4, 5, 6, 7, 8, 9, 1], 1),
        ([9, 1, 2, 3, 4], 1),
    ]

    for i, (nums, expected) in enumerate(test_cases):
        result = find_min(nums)
        assert result == expected, (
            f"Test case {i} failed.\nInput: {nums}\nExpected: {expected}, Got: {result}"
        )

    print("✅ All test cases passed for find_min!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing find_min implementation")
    test_find_min()
