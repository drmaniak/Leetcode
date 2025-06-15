# 🧩 Problem: 3Sum
#
#     Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
#     where nums[i] + nums[j] + nums[k] == 0, and the indices i, j and k are all distinct.
#
#     The output should not contain any duplicate triplets. You may return the output and
#     the triplets in any order.

# ✅ Constraints
#
#     3 <= nums.length <= 1000
#     -10^5 <= nums[i] <= 10^5


def three_sum(nums: list[int]) -> list[list[int]]:
    """
    Find all unique triplets in the array that give the sum of zero.

    Args:
        nums: List of integers

    Returns:
        List of triplets (lists of 3 integers) that sum to zero
    """

    # Sort the numbers
    nums.sort()  # O(nlogn)

    n = len(nums)

    res = []

    for O in range(n):
        # Get the first number (anchor)
        a = nums[O]

        if a > 0:
            break

        # If the anchor is the same as prev anchor
        if O > 0 and a == nums[O - 1]:
            continue

        # Start two pointer search
        L = O + 1
        R = n - 1
        while L < R:
            # Get second and third numbers
            b, c = nums[L], nums[R]
            # Calculate threesum
            threesum = a + b + c

            if threesum < 0:
                L += 1  # move L up to get a larger number
            elif threesum > 0:
                R -= 1  # move R down to get a smaller number
            else:
                # Add numbers to res
                res.append([a, b, c])

                # Move the L & R pointers so that we don't repeat the same numbers
                L += 1
                R -= 1

                # Additionally, increment L so that we don't see duplicate triplets
                while nums[L] == nums[L - 1] and L < R:
                    L += 1
                # Alternatively, we can also scan for duplicates the other way
                # while nums[R] == nums[R+1] and L < R:
                #     R -= 1

    return res


# ✅ Thorough test suite
def test_three_sum():
    # Example 1: [-1,0,1,2,-1,-4] -> [[-1,-1,2],[-1,0,1]]
    result1 = three_sum([-1, 0, 1, 2, -1, -4])
    expected1 = [[-1, -1, 2], [-1, 0, 1]]
    assert_triplets_equal(result1, expected1)

    # Example 2: [0,1,1] -> []
    result2 = three_sum([0, 1, 1])
    expected2 = []
    assert result2 == expected2, f"Expected {expected2}, got {result2}"

    # Example 3: [0,0,0] -> [[0,0,0]]
    result3 = three_sum([0, 0, 0])
    expected3 = [[0, 0, 0]]
    assert_triplets_equal(result3, expected3)

    # Additional test case: [-2,0,1,1,2] -> [[-2,0,2],[-2,1,1]]
    result4 = three_sum([-2, 0, 1, 1, 2])
    expected4 = [[-2, 0, 2], [-2, 1, 1]]
    assert_triplets_equal(result4, expected4)

    # Test case with many duplicates: [-1,-1,-1,0,1,1,1] -> [[-1,-1,2],[-1,0,1]]
    result5 = three_sum([-1, -1, -1, 0, 1, 1, 1])
    expected5 = [[-1, 0, 1]]
    assert_triplets_equal(result5, expected5)

    # Test case with negative numbers: [-3,-2,-1,0,1,2,3] -> [[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,0,1]]
    result6 = three_sum([-3, -2, -1, 0, 1, 2, 3])
    expected6 = [[-3, 0, 3], [-3, 1, 2], [-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
    assert_triplets_equal(result6, expected6)

    # Edge case: Exactly 3 elements that sum to zero
    result7 = three_sum([-1, 0, 1])
    expected7 = [[-1, 0, 1]]
    assert_triplets_equal(result7, expected7)

    # Edge case: Exactly 3 elements that don't sum to zero
    result8 = three_sum([1, 2, 3])
    expected8 = []
    assert result8 == expected8, f"Expected {expected8}, got {result8}"

    print("✅ All test cases passed!")


def assert_triplets_equal(actual, expected):
    """
    Helper function to compare two lists of triplets, ignoring order.

    Args:
        actual: List of triplets returned by the function
        expected: List of expected triplets
    """
    # Sort each triplet and the overall list for consistent comparison
    sorted_actual = [sorted(triplet) for triplet in actual]
    sorted_actual.sort()
    sorted_expected = [sorted(triplet) for triplet in expected]
    sorted_expected.sort()

    assert sorted_actual == sorted_expected, (
        f"Expected {sorted_expected}, got {sorted_actual}"
    )


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing three sum implementation")
    test_three_sum()
