# Given an array nums and a value val, remove all occurrences of val in-place and return the new length of the array.
# Do not allocate extra space for another array — you must do this by modifying the input array in-place with O(1) extra memory.
# The order of elements can be changed, and you don’t need to consider beyond the returned length.


def remove_element(nums: list[int], val: int) -> int:
    """
    Removes all instances of val in nums in-place and returns the new length.
    The order of elements can be changed.
    """

    # array length
    n = len(nums)

    # Edge cases
    if not nums:
        return 0

    left = 0  # Write pointer
    for right in range(n):  # Scan pointer
        curr = nums[right]

        # Use scan pointer to check for condition
        if val != curr:
            nums[left] = curr
            left += 1

    return left


# 🧪 Test cases
nums1 = [3, 2, 2, 3]
k1 = remove_element(nums1, 3)
print(k1, nums1[:k1])  # Expected: 2, [2, 2] (order doesn't matter)

nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
k2 = remove_element(nums2, 2)
print(k2, nums2[:k2])  # Expected: 5, [0, 1, 4, 0, 3] (order doesn't matter)
