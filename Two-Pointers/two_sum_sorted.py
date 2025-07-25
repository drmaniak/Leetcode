# 🧩 Problem: Two Integer Sum II
#
# 🤔 Difficulty: Medium
#
# 🔗 Link: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted
#
#     Given an array of integers numbers that is sorted in non-decreasing order.
#
#     Return the indices (1-indexed) of two numbers, [index1, index2], such that they add up to a given
#     target number target and index1 < index2. Note that index1 and index2 cannot be equal,
#     therefore you may not use the same element twice.
#
#     There will always be exactly one valid solution.
#
#     Your solution must use O(1) additional space.

# ✅ Constraints
#
#     2 <= numbers.length <= 1000
#     -1000 <= numbers[i] <= 1000
#     -1000 <= target <= 1000


def two_sum(numbers: list[int], target: int) -> list[int]:
    """
    Find the indices of two numbers in a sorted array that add up to the target.

    Time Complexity: O(n) where n is the length of the numbers array
    Space Complexity: O(1) as we only use two pointers

    Args:
        numbers: A sorted array of integers
        target: The target sum

    Returns:
        A list containing the 1-indexed positions of the two numbers
    """

    n = len(numbers)

    L = 0
    R = n - 1

    while L <= R:
        twosum = numbers[L] + numbers[R]

        if twosum < target:
            L += 1
        elif twosum > target:
            R -= 1
        else:
            return [L + 1, R + 1]

    return [-1, -1]


# ✅ Thorough test suite
def test_two_sum():
    # Example 1: [1,2,3,4], target = 3
    assert two_sum([1, 2, 3, 4], 3) == [1, 2]

    # Example with negative numbers
    assert two_sum([-3, -2, -1, 0, 1, 2], -5) == [1, 2]

    # Example with duplicate numbers
    # Our implementation returns the first matching pair
    assert two_sum([1, 1, 2, 3, 4], 5) == [1, 5]

    # Example with larger numbers
    assert two_sum([10, 20, 30, 40, 50], 60) == [1, 5]

    # Example with all numbers being the same
    # Our implementation uses the first and last numbers
    assert two_sum([2, 2, 2, 2], 4) == [1, 4]

    # Example with target at the extremes
    assert two_sum([1, 2, 3, 4, 5], 9) == [4, 5]

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing two sum implementations for sorted arrays")
    test_two_sum()
