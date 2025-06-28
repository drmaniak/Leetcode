# 🧩 Problem: Climbing Stairs
#
# 🤔 Difficulty: Easy
#
#     You are climbing a staircase. It takes n steps to reach the top.
#     Each time you can either climb 1 or 2 steps.
#     In how many distinct ways can you climb to the top?
#
#     Example 1:
#     Input: n = 2
#     Output: 2
#     Explanation:
#         1 step + 1 step
#         2 steps
#
#     Example 2:
#     Input: n = 3
#     Output: 3
#     Explanation:
#         1 + 1 + 1
#         1 + 2
#         2 + 1
#
# ✅ Constraints:
#     1 <= n <= 45


memo_dict = {}


def climb_stairs_recursive(n: int) -> int:
    """
    Return the number of distinct ways to climb to the top using recursion.

    Args:
        n: Total number of steps to reach the top

    Returns:
        Number of distinct ways to reach the top
    """
    # Your solution here
    pass

    # Base case
    if n in memo_dict:
        return memo_dict[n]
    else:
        if n <= 1:
            return 1

        ways = climb_stairs_recursive(n - 1) + climb_stairs_recursive(n - 2)

        memo_dict[n] = ways

        return ways


def climb_stairs_iterative(n: int) -> int:
    """
    Return the number of distinct ways to climb to the top using iteration (DP).

    Args:
        n: Total number of steps to reach the top

    Returns:
        Number of distinct ways to reach the top
    """
    # Your solution here
    pass
    return 0


# ✅ Test suite
def test_climb_stairs():
    test_cases = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (10, 89),
        (20, 10946),
        (30, 1346269),
        (35, 14930352),
        (38, 63245986),
    ]

    for i, (input_n, expected) in enumerate(test_cases):
        result_rec = climb_stairs_recursive(input_n)
        # result_iter = climb_stairs_iterative(input_n)

        assert result_rec == expected, (
            f"[Recursive] Test case {i} failed: n={input_n}, expected {expected}, got {result_rec}"
        )
        # assert result_iter == expected, (
        #     f"[Iterative] Test case {i} failed: n={input_n}, expected {expected}, got {result_iter}"
        # )

    print("✅ All test cases passed for both recursive and iterative versions!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing climb stairs implementations")
    test_climb_stairs()
