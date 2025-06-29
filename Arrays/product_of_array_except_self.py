# 🧩 Problem: Product of Array Except Self
#
# 🤔 Difficulty: Medium
#
# 🔗 Link: https://leetcode.com/problems/product-of-array-except-self
#
#     Given an integer array nums, return an array output where output[i] is the product
#     of all the elements of nums except nums[i].
#     Each product is guaranteed to fit in a 32-bit integer.
#
# Follow-up: Could you solve it in O(n) time without using the division operation?

# ✅ Constraints
#
#     2 <= nums.length <= 1000
#
#     -20 <= nums[i] <= 20
#


def product_except_self(nums: list[int]) -> list[int]:
    """
    Returns an array where each element at index i is the product of all elements
    in nums except the one at index i.

    Time Complexity: O(n)
    Space Complexity: O(1) excluding the output array
    """

    n = len(nums)

    lprod = 1
    rprod = 1

    output = [1] * n

    for i in range(n):
        L = i
        R = n - i - 1

        output[L] *= lprod
        output[R] *= rprod

        lprod *= nums[L]
        rprod *= nums[R]

    return output


# ✅ Thorough test suite
def test_product_except_self():
    # Example 1
    nums1 = [1, 2, 4, 6]
    result1 = product_except_self(nums1)
    assert result1 == [48, 24, 12, 8]

    # Example 2
    nums2 = [-1, 0, 1, 2, 3]
    result2 = product_except_self(nums2)
    assert result2 == [0, -6, 0, 0, 0]

    # Additional test cases
    nums3 = [1, 2, 3, 4]
    result3 = product_except_self(nums3)
    assert result3 == [24, 12, 8, 6]

    nums4 = [2, 2, 2, 2]
    result4 = product_except_self(nums4)
    assert result4 == [8, 8, 8, 8]

    nums5 = [0, 0, 0]
    result5 = product_except_self(nums5)
    assert result5 == [0, 0, 0]

    nums6 = [-1, -1, -1, -1]
    result6 = product_except_self(nums6)
    assert result6 == [-1, -1, -1, -1]

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    test_product_except_self()
