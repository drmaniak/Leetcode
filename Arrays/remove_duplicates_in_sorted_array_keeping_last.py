# 🧩 Problem: Remove All Duplicates Except One (Sorted Array)
#
# 🤔 Difficulty: Easy
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


def remove_all_but_last_duplicates(nums: list[int]) -> int:
    """
    Removes all duplicates from a sorted array in-place, keeping only the *last* occurrence
    of each element. Returns the new length of the array.

    """

    n = len(nums)

    if n <= 1:
        return n

    L = 0
    R = 1

    while R < n:
        if nums[R] != nums[R - 1]:
            nums[L] = nums[R - 1]
            L += 1
        R += 1
    nums[L] = nums[R - 1]
    return L + 1


# ✅ Thorough test suite
def test_remove_all_but_last_duplicates():
    nums1 = [1, 1, 2]
    k1 = remove_all_but_last_duplicates(nums1)
    assert k1 == 2
    assert nums1[:k1] == [1, 2]

    nums2 = [1, 1, 1, 2, 2, 3]
    k2 = remove_all_but_last_duplicates(nums2)
    assert k2 == 3
    assert nums2[:k2] == [1, 2, 3]

    nums3 = [0, 0, 1, 1, 2, 3, 3, 3, 4]
    k3 = remove_all_but_last_duplicates(nums3)
    assert k3 == 5
    assert nums3[:k3] == [0, 1, 2, 3, 4]

    nums4 = [1, 2, 3, 4, 5]
    k4 = remove_all_but_last_duplicates(nums4)
    assert k4 == 5
    assert nums4[:k4] == [1, 2, 3, 4, 5]

    nums5 = [1, 1, 1, 1, 1]
    k5 = remove_all_but_last_duplicates(nums5)
    assert k5 == 1
    assert nums5[:k5] == [1]

    nums6 = []
    k6 = remove_all_but_last_duplicates(nums6)
    assert k6 == 0
    assert nums6[:k6] == []

    nums7 = [7]
    k7 = remove_all_but_last_duplicates(nums7)
    assert k7 == 1
    assert nums7[:k7] == [7]

    nums8 = [2, 2, 3, 3, 4, 4]
    k8 = remove_all_but_last_duplicates(nums8)
    assert k8 == 3
    assert nums8[:k8] == [2, 3, 4]

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    test_remove_all_but_last_duplicates()
