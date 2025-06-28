# 🧩 Problem: Best Time to Buy and Sell Stock
#
# 🤔 Difficulty: Easy
#
#     You are given an integer array `prices` where `prices[i]` is the price of NeetCoin on the i-th day.
#
#     You may choose a single day to buy one NeetCoin and choose a different day in the future to sell it.
#
#     Return the maximum profit you can achieve. If no profit is possible, return 0.
#
#     Example 1:
#         Input:  prices = [10, 1, 5, 6, 7, 1]
#         Output: 6
#         Explanation: Buy at price[1] = 1, sell at price[4] = 7, profit = 6
#
#     Example 2:
#         Input:  prices = [10, 8, 7, 5, 2]
#         Output: 0
#         Explanation: No profitable transaction possible
#
# ✅ Constraints:
#     - 1 <= prices.length <= 100
#     - 0 <= prices[i] <= 100

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Calculate the maximum profit from buying and selling NeetCoin once.

    Args:
        prices: List of prices where prices[i] is the price on the i-th day

    Returns:
        The maximum profit achievable; 0 if no transaction is profitable
    """
    # Your solution here

    n = len(prices)

    if n <= 1:
        return 0

    BUY = 0
    SELL = 1
    maxp = 0

    while SELL < n:
        if prices[BUY] < prices[SELL]:
            profit = prices[SELL] - prices[BUY]
            maxp = max(profit, maxp)
        else:
            BUY = SELL

        SELL += 1

    return maxp


# ✅ Test suite
def test_max_profit():
    test_cases = [
        ([10, 1, 5, 6, 7, 1], 6),
        ([10, 8, 7, 5, 2], 0),
        ([1, 2, 3, 4, 5], 4),
        ([5, 4, 3, 2, 1], 0),
        ([3, 2, 6, 1, 4], 4),
        ([7, 1, 5, 3, 6, 4], 5),  # buy at 1, sell at 6
        ([2, 4, 1], 2),  # buy at 2, sell at 4
        ([2], 0),  # only one price
        ([3, 3, 3, 3], 0),  # constant prices
        ([1, 100], 99),  # best case
    ]

    for i, (prices, expected) in enumerate(test_cases):
        result = max_profit(prices)
        assert result == expected, (
            f"Test case {i} failed.\nPrices: {prices}\nExpected: {expected}, Got: {result}"
        )

    print("✅ All test cases passed for max_profit!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing max_profit implementation")
    test_max_profit()
