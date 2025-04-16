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

    # 2 pointer appraoch
    left = 0
    for right in range(n):
        curr = nums[right]

        # Write condition
        if curr != val:
            nums[left] = curr
            left += 1

    return left


def test_remove_element():
    # 🧪 Basic test
    nums1 = [3, 2, 2, 3]
    k1 = remove_element(nums1, 3)
    assert k1 == 2
    assert sorted(nums1[:k1]) == [2, 2]

    # 🧪 Mixed values, val scattered
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    k2 = remove_element(nums2, 2)
    assert k2 == 5
    assert sorted(nums2[:k2]) == sorted([0, 1, 3, 0, 4])

    # 🧪 All values are val
    nums3 = [5, 5, 5, 5]
    k3 = remove_element(nums3, 5)
    assert k3 == 0
    assert nums3[:k3] == []

    # 🧪 No values to remove
    nums4 = [1, 2, 3, 4]
    k4 = remove_element(nums4, 9)
    assert k4 == 4
    assert sorted(nums4[:k4]) == [1, 2, 3, 4]

    # 🧪 Empty list
    nums5 = []
    k5 = remove_element(nums5, 1)
    assert k5 == 0
    assert nums5[:k5] == []

    # 🧪 Single element, match
    nums6 = [7]
    k6 = remove_element(nums6, 7)
    assert k6 == 0
    assert nums6[:k6] == []

    # 🧪 Single element, no match
    nums7 = [8]
    k7 = remove_element(nums7, 3)
    assert k7 == 1
    assert nums7[:k7] == [8]

    # 🧪 All values different, some match
    nums8 = [10, 11, 12, 13, 14]
    k8 = remove_element(nums8, 12)
    assert k8 == 4
    assert sorted(nums8[:k8]) == [10, 11, 13, 14]

    # 🧪 Large input (stress test)
    nums9 = [1] * 10000 + [2] * 10000 + [3] * 10000
    k9 = remove_element(nums9, 2)
    assert k9 == 20000
    assert all(x != 2 for x in nums9[:k9])
    assert sorted(nums9[:k9]) == [1] * 10000 + [3] * 10000

    print("✅ All test cases passed!")


if __name__ == "__main__":
    test_remove_element()
