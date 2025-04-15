# 🧩 Problem: Remove All Duplicates Except One (Sorted Array)
#
#     Given a sorted array nums, modify it in-place such that each element appears at most once — but you must preserve the relative order of the unique elements. Return the new length of the array after duplicates are removed.
#     You must not allocate extra space — the operation must be done with O(1) extra memory.
#
# This is a soft twist on the original removeDuplicates problem — same core logic, new framing to deepen your grasp.

# ✅ Constraints
#
#     1 <= len(nums) <= 10^5
#
#     -10^4 <= nums[i] <= 10^4
#
#     nums is sorted in non-decreasing order.


def remove_all_duplicates(nums: list[int]) -> int:
    """
    Given a sorted array nums, remove all duplicates in-place so each element appears only once.
    Return the new length of the array.
    You must do this in-place with O(1) extra memory.
    """

    # Length of array
    n = len(nums)
    # Edge cases when len(nums) <= 1
    if n <= 1:
        return len(nums)

    # 2 pointer method
    # Initialize 2 pointers, one to scan through the array, one to keep track of the idx to write
    # These pointers can be initialized based on where we need to start scanning from
    # In this problem, we never touch the first element, so we can start from idx=1
    # The scanner pointer compares against the previous element, if it's not a duplicate, it writes at the idx of the second pointer
    # The second pointer is incremented

    left = 1
    for right in range(1, n):
        curr = nums[right]
        prev = nums[right - 1]

        if curr != prev:
            nums[left] = curr
            left += 1

    return left


# ✅ Test cases
def test_remove_all_duplicates():
    nums1 = [1, 1, 2]
    k1 = remove_all_duplicates(nums1)
    assert k1 == 2
    assert nums1[:k1] == [1, 2]

    nums2 = [0, 0, 1, 1, 2, 3, 3, 4]
    k2 = remove_all_duplicates(nums2)
    assert k2 == 5
    assert nums2[:k2] == [0, 1, 2, 3, 4]

    nums3 = [1, 2, 3, 4, 5]
    k3 = remove_all_duplicates(nums3)
    assert k3 == 5
    assert nums3[:k3] == [1, 2, 3, 4, 5]

    nums4 = [1, 1, 1, 1, 1]
    k4 = remove_all_duplicates(nums4)
    assert k4 == 1
    assert nums4[:k4] == [1]

    nums5 = []
    k5 = remove_all_duplicates(nums5)
    assert k5 == 0
    assert nums5[:k5] == []

    nums6 = [1]
    k6 = remove_all_duplicates(nums6)
    assert k6 == 1
    assert nums6[:k6] == [1]

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    test_remove_all_duplicates()
