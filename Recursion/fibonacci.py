# 🧩 Problem: Fibonacci Number
#
# 🤔 Difficulty: Easy
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

from functools import lru_cache


@lru_cache
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
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_optimized(n: int) -> int:
    """
    Calculate the nth Fibonacci number using an optimized approach.

    This function should implement a more efficient algorithm than
    the naive recursive approach, such as using memoization or an
    iterative solution.

    Args:
        n: A non-negative integer

    Returns:
        The nth Fibonacci number
    """
    # Your optimized solution here

    if n <= 1:
        return n

    # store the n-1 and n-2 fibo values
    fibo_2 = 0
    fibo_1 = 1

    # Store a var for final fibo
    fibo = 0
    for i in range(2, n + 1):
        # fibo(n) is given as fibo(n-1) + fibo(n-2)
        fibo = fibo_2 + fibo_1

        fibo_2 = fibo_1
        fibo_1 = fibo

    return fibo


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

    if test_optimized:
        # Test optimized solution with the same cases
        assert fibonacci_optimized(0) == 0, "Optimized F(0) should be 0"
        assert fibonacci_optimized(1) == 1, "Optimized F(1) should be 1"
        assert fibonacci_optimized(2) == 1, "Optimized F(2) should be 1"
        assert fibonacci_optimized(5) == 5, "Optimized F(5) should be 5"
        assert fibonacci_optimized(8) == 21, "Optimized F(8) should be 21"

        # Test larger values (may be slow with naive recursion)
        assert fibonacci_optimized(10) == 55, "Optimized F(10) should be 55"
        assert fibonacci_optimized(15) == 610, "Optimized F(15) should be 610"
        assert fibonacci_optimized(20) == 6765, "Optimized F(20) should be 6765"
        assert fibonacci_optimized(25) == 75025, "Optimized F(25) should be 75025"
        assert fibonacci_optimized(30) == 832040, "Optimized F(30) should be 832040"

    print("✅ All test cases passed!")


# 🧪 Performance comparison
def compare_performance(n: int = 20):
    """Compare the performance of both implementations for calculating F(n)."""
    import time

    # Time the recursive implementation (only for smaller values)
    if n <= 50:  # Limit to avoid excessive runtime
        start = time.time()
        result_recursive = fibonacci(n)
        end = time.time()
        recursive_time = end - start
        print(
            f"Recursive F({n}) = {result_recursive}, Time: {recursive_time:.6f} seconds"
        )
    else:
        print(f"Skipping recursive implementation for n={n} (too slow)")
        recursive_time = float("inf")

    # Time the optimized implementation
    start = time.time()
    result_optimized = fibonacci_optimized(n)
    end = time.time()
    optimized_time = end - start
    print(f"Optimized F({n}) = {result_optimized}, Time: {optimized_time:.6f} seconds")

    # Calculate speedup
    if recursive_time != float("inf"):
        speedup = (
            recursive_time / optimized_time if optimized_time > 0 else float("inf")
        )
        print(f"Speedup: {speedup:.2f}x")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing Fibonacci implementations")
    test_fibonacci()
    test_fibonacci(test_optimized=True)

    print("\nComparing performance:")
    compare_performance(10)  # Compare for F(10)
    compare_performance(20)  # Compare for F(20)
    # Uncomment to test larger values (will only use optimized version)
    compare_performance(30)
    compare_performance(50)
