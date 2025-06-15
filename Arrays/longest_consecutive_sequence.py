# 🧩 Problem: Longest Consecutive Sequence
#
#     Given an array of integers nums, return the length of the longest consecutive sequence
#     of elements that can be formed.
#
#     A consecutive sequence is a sequence of elements in which each element is exactly 1 greater
#     than the previous element. The elements do not have to be consecutive in the original array.
#
#     You must write an algorithm that runs in O(n) time.

# ✅ Constraints
#
#     0 <= nums.length <= 1000
#     -10^9 <= nums[i] <= 10^9


def longest_consecutive(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive sequence of elements.

    Time Complexity: O(n) where n is the length of nums
    Space Complexity: O(n) for the hashset

    Args:
        nums: List of integers

    Returns:
        Length of the longest consecutive sequence
    """

    if not nums:
        return 0

    numset = set(nums)

    longest = 0

    for num in nums:
        if (num - 1) not in numset:
            length = 0
            while (num + length) in numset:
                length += 1

            longest = max(longest, length)

    return longest


# NOTE: AI GENERATED
# Alternative approach using a hash map
def longest_consecutive_map(nums: list[int]) -> int:
    """
    Find the length of the longest consecutive sequence using a hash map approach.

    Time Complexity: O(n) where n is the length of nums
    Space Complexity: O(n) for the hash map

    Args:
        nums: List of integers

    Returns:
        Length of the longest consecutive sequence
    """
    if not nums:
        return 0

    # Create a hash map to track sequence lengths
    # Key: number, Value: length of consecutive sequence
    length_map = {}
    max_length = 0

    for num in nums:
        # Skip if we've already processed this number
        if num in length_map:
            continue

        # Check if there are consecutive numbers before and after
        left_length = length_map.get(num - 1, 0)
        right_length = length_map.get(num + 1, 0)

        # Current sequence length is the sum of left and right sequences plus 1
        current_length = left_length + right_length + 1

        # Update max_length
        max_length = max(max_length, current_length)

        # Update the length for the current number
        length_map[num] = current_length

        # Update the length for the boundary numbers of the sequence
        # This extends the sequence at both ends
        length_map[num - left_length] = current_length
        length_map[num + right_length] = current_length

    return max_length


# ✅ Thorough test suite
def test_longest_consecutive():
    # Example 1: [2,20,4,10,3,4,5] -> [2,3,4,5] is the longest consecutive sequence
    assert longest_consecutive([2, 20, 4, 10, 3, 4, 5]) == 4
    assert longest_consecutive_map([2, 20, 4, 10, 3, 4, 5]) == 4

    # Example 2: [0,3,2,5,4,6,1,1] -> [0,1,2,3,4,5,6] is the longest consecutive sequence
    assert longest_consecutive([0, 3, 2, 5, 4, 6, 1, 1]) == 7
    assert longest_consecutive_map([0, 3, 2, 5, 4, 6, 1, 1]) == 7

    # Empty array
    assert longest_consecutive([]) == 0
    assert longest_consecutive_map([]) == 0

    # Single element
    assert longest_consecutive([5]) == 1
    assert longest_consecutive_map([5]) == 1

    # Duplicate elements
    assert longest_consecutive([1, 1, 1, 1]) == 1
    assert longest_consecutive_map([1, 1, 1, 1]) == 1

    # Negative numbers
    assert longest_consecutive([-3, -2, -1, 0, 1]) == 5
    assert longest_consecutive_map([-3, -2, -1, 0, 1]) == 5

    # Large gaps
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4
    assert longest_consecutive_map([100, 4, 200, 1, 3, 2]) == 4

    # Multiple sequences
    assert longest_consecutive([1, 2, 3, 10, 11, 12, 13]) == 4
    assert longest_consecutive_map([1, 2, 3, 10, 11, 12, 13]) == 4

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing longest consecutive sequence implementations")
    test_longest_consecutive()
