# 🧩 Problem: Evaluate Reverse Polish Notation
#
#     You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.
#
#     Return the integer that represents the evaluation of the expression.
#
#     The operands may be integers or the results of other operations.
#     The operators include '+', '-', '*', and '/'.
#     Assume that division between integers always truncates toward zero.
#
#     Example 1:
#     Input: tokens = ["1","2","+","3","*","4","-"]
#     Output: 5
#     Explanation: ((1 + 2) * 3) - 4 = 5

# ✅ Constraints
#
#     1 <= tokens.length <= 1000
#     tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100]


def evaluate_rpn(tokens: list[str]) -> int:
    """
    Evaluate the given Reverse Polish Notation expression.

    Args:
        tokens: A list of strings representing a valid arithmetic expression in RPN
                Each token is either an operator ("+", "-", "*", "/") or an integer

    Returns:
        The integer result of evaluating the expression
    """
    # Your solution here

    rpn_stack = []

    valid_ops = set(["+", "-", "*", "/"])

    for char in tokens:
        if char not in valid_ops:
            rpn_stack.append(int(char))
        else:
            n2 = rpn_stack.pop()
            n1 = rpn_stack.pop()
            out = calculate(char, n1, n2)

            rpn_stack.append(out)

    return rpn_stack[-1]


def calculate(op: str, n1: int, n2: int) -> int:
    res = 0

    if op == "+":
        res = n1 + n2
    elif op == "-":
        res = n1 - n2
    elif op == "*":
        res = n1 * n2
    elif op == "/":
        res = n1 / n2

    return int(res)


# ✅ Thorough test suite
def test_evaluate_rpn():
    # Example 1: ["1","2","+","3","*","4","-"] -> 5
    # Explanation: ((1 + 2) * 3) - 4 = 5
    assert evaluate_rpn(["1", "2", "+", "3", "*", "4", "-"]) == 5, "Example 1 failed"

    # Example 2: ["2","1","+","3","*"] -> 9
    # Explanation: (2 + 1) * 3 = 9
    assert evaluate_rpn(["2", "1", "+", "3", "*"]) == 9, "Example 2 failed"

    # Example 3: ["4","13","5","/","+"] -> 5
    # Explanation: 4 + (13 / 5) = 4 + 2 = 6
    assert evaluate_rpn(["4", "13", "5", "/", "+"]) == 6, "Example 3 failed"

    # Example 4: ["10","6","9","3","+","-11","*","/","*","17","+","5","+"] -> 22
    # Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5 = 22
    assert (
        evaluate_rpn(
            ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
        )
        == 22
    ), "Example 4 failed"

    # Single number
    assert evaluate_rpn(["42"]) == 42, "Single number case failed"

    # Addition
    assert evaluate_rpn(["3", "4", "+"]) == 7, "Simple addition failed"

    # Subtraction
    assert evaluate_rpn(["5", "2", "-"]) == 3, "Simple subtraction failed"

    # Multiplication
    assert evaluate_rpn(["7", "3", "*"]) == 21, "Simple multiplication failed"

    # Division with truncation toward zero
    assert evaluate_rpn(["7", "2", "/"]) == 3, "Division with truncation failed"

    # Negative division with truncation toward zero
    assert evaluate_rpn(["-7", "2", "/"]) == -3, (
        "Negative division with truncation failed"
    )

    # More complex expressions
    assert evaluate_rpn(["3", "4", "+", "2", "*", "7", "/"]) == 2, (
        "Complex expression 1 failed"
    )

    # Expression with negative numbers
    assert evaluate_rpn(["-3", "-4", "+", "-5", "*"]) == 35, (
        "Negative numbers expression failed"
    )

    # Expression with multiple operations
    assert evaluate_rpn(["5", "1", "2", "+", "4", "*", "+", "3", "-"]) == 14, (
        "Multiple operations failed"
    )

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing Reverse Polish Notation evaluation")
    test_evaluate_rpn()
