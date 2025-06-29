# 🧩 Problem: Koko Eating Bananas
#
# 🤔 Difficulty: Medium
#
# 🔗 Link: https://leetcode.com/problems/koko-eating-bananas
#
#     You are given an integer array `piles` where `piles[i]` is the number of bananas in the ith pile.
#     You are also given an integer `h`, the total number of hours you have to eat all the bananas.
#
#     You may decide your bananas-per-hour eating rate `k`.
#     Each hour, you may choose any pile and eat up to `k` bananas from it.
#     If the pile has less than `k` bananas, you eat the entire pile and cannot continue to another in the same hour.
#
#     Return the **minimum integer `k`** such that Koko can eat all the bananas within `h` hours.
#
#     Example 1:
#         Input:  piles = [1, 4, 3, 2], h = 9
#         Output: 2
#
#     Example 2:
#         Input:  piles = [25, 10, 23, 4], h = 4
#         Output: 25
#
# ✅ Constraints:
#     - 1 <= piles.length <= 1000
#     - piles.length <= h <= 1_000_000
#     - 1 <= piles[i] <= 1_000_000_000

import math
from typing import List


def min_eating_speed(piles: List[int], h: int) -> int:
    """
    Find the minimum bananas-per-hour speed `k` such that all bananas are eaten in `h` hours.

    Args:
        piles: List of piles, where piles[i] is the number of bananas in the i-th pile
        h: Total number of hours available

    Returns:
        The minimum integer k such that all bananas are eaten within h hours
    """
    # Your solution here

    low = 1
    high = max(piles)

    min_speed = 0

    while low <= high:
        speed = (high + low) // 2

        times = [math.ceil(pile / speed) for pile in piles]
        current_h = sum(times)
        if current_h <= h:
            min_speed = speed
            high = speed - 1
        else:
            low = speed + 1
    return min_speed


# ✅ Test suite
def test_min_eating_speed():
    test_cases = [
        ([3, 6, 7, 11], 8, 4),
        ([1, 4, 3, 2], 9, 2),
        ([25, 10, 23, 4], 4, 25),
        ([30, 11, 23, 4, 20], 6, 23),
        ([3, 6, 7, 11], 8, 4),
        ([3, 6, 7, 11], 5, 7),
        ([1000000000], 2, 500000000),
        ([1] * 1000, 1000, 1),
        ([1_000_000_000] * 1000, 1_000_000, 1_000_000),
    ]

    for i, (piles, h, expected) in enumerate(test_cases):
        result = min_eating_speed(piles, h)
        assert result == expected, (
            f"Test case {i} failed.\nPiles: {piles}, h: {h}\nExpected: {expected}, Got: {result}"
        )

    print("✅ All test cases passed for Koko Eating Bananas!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing min_eating_speed implementation")
    test_min_eating_speed()
