# 🧩 Problem: Container With Most Water
#
# 🤔 Difficulty: Medium
#
#     You are given an integer array heights where heights[i] represents the height of the ith bar.
#
#     You may choose any two bars to form a container. Return the maximum amount of water a container can store.
#
#     Note: The amount of water a container can store is calculated as:
#     min(heights[i], heights[j]) * (j - i)
#     where i and j are the indices of the two bars.

# ✅ Constraints
#
#     2 <= height.length <= 1000
#     0 <= height[i] <= 1000


def most_water(heights: list[int]) -> int:
    """
    Find the maximum area of water that can be contained between two bars.

    Args:
        heights: List of integer heights

    Returns:
        Maximum area of water
    """

    n = len(heights)

    L = 0
    R = n - 1

    most_water = 0

    while L < R:
        hL = heights[L]
        hR = heights[R]
        current_water = min(hL, hR) * (R - L)
        if hL < hR:
            L += 1
        else:
            R -= 1

        most_water = max(most_water, current_water)

    return most_water


# ✅ Thorough test suite
def test_most_water():
    # Example 1: [1,7,2,5,4,7,3,6] -> 36
    assert most_water([1, 7, 2, 5, 4, 7, 3, 6]) == 36, "Example 1 failed"

    # Example 2: [2,2,2] -> 4
    assert most_water([2, 2, 2]) == 4, "Example 2 failed"

    # Edge case: Minimum length [2, 3] -> 2
    assert most_water([2, 3]) == 2, "Minimum length case failed"

    # Edge case: All zeros [0, 0, 0, 0] -> 0
    assert most_water([0, 0, 0, 0]) == 0, "All zeros case failed"

    # Case with max height at edges [9, 1, 2, 3, 10] -> 36
    assert most_water([9, 1, 2, 3, 10]) == 36, "Max height at edges case failed"

    # Decreasing heights [6, 5, 4, 3, 2, 1] -> 9
    assert most_water([6, 5, 4, 3, 2, 1]) == 9, "Decreasing heights case failed"

    # Increasing heights [1, 2, 3, 4, 5, 6] -> 9
    assert most_water([1, 2, 3, 4, 5, 6]) == 9, "Increasing heights case failed"

    # Case with tallest in middle [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
    assert most_water([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49, (
        "Tallest in middle case failed"
    )

    # Case with same height bars far apart [4, 3, 2, 1, 4] -> 16
    assert most_water([4, 3, 2, 1, 4]) == 16, "Same height bars far apart case failed"

    # Large difference in heights [1, 1000, 1, 1, 1, 1, 1] -> 6
    assert most_water([1, 1000, 1, 1, 1, 1, 1]) == 6, (
        "Large difference in heights case failed"
    )

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing container with most water implementation")
    test_most_water()
