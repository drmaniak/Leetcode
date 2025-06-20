# 🧩 Problem: Fibonacci Number
#
#     The Fibonacci numbers, commonly denoted F(n), form a sequence where each number
#     is the sum of the two preceding ones, starting from 0 and 1.
#
#     F(0) = 0, F(1) = 1
#     F(n) = F(n-1) + F(n-2), for n > 1.
#
#     Given n, calculate F(n).
#
#     Example 1:
#     Input: n = 2
#     Output: 1
#     Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
#
#     Example 2:
#     Input: n = 3
#     Output: 2
#     Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
#
#     Example 3:
#     Input: n = 4
#     Output: 3
#     Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.

# ✅ Constraints
#
#     0 <= n <= 30
#
# 🔍 Notes on Recursion
#
#     This problem is excellent for practicing recursion because:
#     1. It has a clear recursive definition: F(n) = F(n-1) + F(n-2)
#     2. It has well-defined base cases: F(0) = 0, F(1) = 1
#     3. Each recursive call reduces the problem size
#
#     However, a naive recursive solution can be inefficient due to redundant calculations.
#     Consider how you might optimize your recursive approach using techniques like:
#     - Memoization (storing previously computed results)
#     - Tail recursion
#     - Or converting to an iterative solution


def fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number using recursion.

    The Fibonacci sequence is defined as:
    F(0) = 0, F(1) = 1
    F(n) = F(n-1) + F(n-2), for n > 1

    Args:
        n: A non-negative integer

    Returns:
        The nth Fibonacci number
    """
    # Your recursive solution here

    # Base case
    if n in [0, 1]:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)



# ✅ Thorough test suite
def test_fibonacci(test_optimized=False):
    # Test basic cases
    assert fibonacci(0) == 0, "F(0) should be 0"
    assert fibonacci(1) == 1, "F(1) should be 1"
    assert fibonacci(2) == 1, "F(2) should be 1"
    assert fibonacci(3) == 2, "F(3) should be 2"
    assert fibonacci(4) == 3, "F(4) should be 3"
    assert fibonacci(5) == 5, "F(5) should be 5"

    # Test a few more cases
    assert fibonacci(6) == 8, "F(6) should be 8"
    assert fibonacci(7) == 13, "F(7) should be 13"
    assert fibonacci(8) == 21, "F(8) should be 21"


    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing Fibonacci implementations")
    test_fibonacci()
