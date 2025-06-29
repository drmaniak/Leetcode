# 🧩 Problem: Remove All Duplicates Except One (Sorted Array)
#
# 🤔 Difficulty: Easy
#
# 🔗 Link:
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

    n = len(nums)

    if n <= 1:
        return n

    # Initialize Read & Write pointers
    L = 0
    R = 1

    while R < n:
        if nums[L] != nums[R]:
            L += 1
            nums[L] = nums[R]
        R += 1

    return L + 1


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
