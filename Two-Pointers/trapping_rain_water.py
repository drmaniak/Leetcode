# 🧩 Problem: Trapping Rain Water
#
#     You are given an array of non-negative integers height which represent an elevation map.
#     Each value height[i] represents the height of a bar, which has a width of 1.
#
#     Return the maximum area of water that can be trapped between the bars.

# ✅ Constraints
#
#     1 <= height.length <= 1000
#     0 <= height[i] <= 1000


def trap(height: list[int]) -> int:
    """
    Calculate the amount of water that can be trapped between the bars.

    Args:
        height: List of non-negative integers representing bar heights

    Returns:
        The total amount of water trapped
    """
    # Your solution here

    if len(height) <= 2:
        return 0

    n = len(height)

    prefix = [0] * n
    for i in range(1, n):
        prefix[i] = max(prefix[i - 1], height[i - 1])

    suffix = [0] * n
    for i in range(n - 2, -1, -1):
        suffix[i] = max(suffix[i + 1], height[i + 1])

    total_height = 0

    for i in range(n):
        val = max(min(prefix[i], suffix[i]) - height[i], 0)
        total_height += val

    return total_height


# ✅ Thorough test suite
def test_trap():
    # Example 1: [0,2,0,3,1,0,1,3,2,1] -> 9
    assert trap([0, 2, 0, 3, 1, 0, 1, 3, 2, 1]) == 9, "Example 1 failed"

    # Simple case: [0,1,0,2,1,0,1,3,2,1,2,1] -> 6
    assert trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6, "Simple case failed"

    # Edge case: No trapped water [1,2,3,4,5] -> 0
    assert trap([1, 2, 3, 4, 5]) == 0, "Increasing heights case failed"

    # Edge case: No trapped water [5,4,3,2,1] -> 0
    assert trap([5, 4, 3, 2, 1]) == 0, "Decreasing heights case failed"

    # Edge case: Single element [5] -> 0
    assert trap([5]) == 0, "Single element case failed"

    # Edge case: Two elements [5,2] -> 0
    assert trap([5, 2]) == 0, "Two elements case failed"

    # Case with plateaus [3,3,3,3,3] -> 0
    assert trap([3, 3, 3, 3, 3]) == 0, "Plateau case failed"

    # Case with equal height walls and valley [3,0,3] -> 3
    assert trap([3, 0, 3]) == 3, "Equal height walls case failed"

    # Case with multiple peaks and valleys [4,2,0,3,2,5] -> 9
    assert trap([4, 2, 0, 3, 2, 5]) == 9, "Multiple peaks and valleys case failed"

    # Large example with various heights
    assert (
        trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0, 4, 2, 0, 3, 2, 5, 0, 1, 2]) == 26
    ), "Large example failed"

    # Case with zeros at beginning and end [0,1,2,3,2,1,0] -> 0
    assert trap([0, 1, 2, 3, 2, 1, 0]) == 0, "Zeros at beginning and end case failed"

    # Case with all zeros [0,0,0,0] -> 0
    assert trap([0, 0, 0, 0]) == 0, "All zeros case failed"

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing trapping rain water implementation")
    test_trap()
