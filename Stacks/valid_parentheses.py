# 🧩 Problem: Valid Parentheses
#
#     You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
#
#     The input string s is valid if and only if:
#         1. Every open bracket is closed by the same type of close bracket.
#         2. Open brackets are closed in the correct order.
#         3. Every close bracket has a corresponding open bracket of the same type.
#
#     Return true if s is a valid string, and false otherwise.

# ✅ Constraints
#
#     1 <= s.length <= 1000


def is_valid(s: str) -> bool:
    """
    Determine if the input string has valid parentheses.

    Args:
        s: A string containing only parentheses characters: '(', ')', '{', '}', '[', ']'

    Returns:
        True if the string has valid parentheses, False otherwise
    """
    # Your solution here

    closepairs = {
        "]": "[",
        ")": "(",
        "}": "{",
    }

    stack = []

    for char in s:
        if char in closepairs:
            if not stack:
                return False

            if closepairs[char] != stack[-1]:
                return False

            stack.pop()
        else:
            stack.append(char)

    return not stack


# ✅ Thorough test suite
def test_is_valid():
    # Example 1: "[]" -> true
    assert is_valid("[]") == True, "Example 1 failed"

    # Example 2: "([{}])" -> true
    assert is_valid("([{}])") == True, "Example 2 failed"

    # Example 3: "[(])" -> false
    assert is_valid("[(])") == False, "Example 3 failed"

    # Empty string -> true (no brackets to validate)
    assert is_valid("") == True, "Empty string case failed"

    # Single opening bracket -> false (no closing bracket)
    assert is_valid("(") == False, "Single opening bracket case failed"

    # Single closing bracket -> false (no opening bracket)
    assert is_valid(")") == False, "Single closing bracket case failed"

    # Multiple types of brackets -> true
    assert is_valid("()[]{}") == True, "Multiple bracket types case failed"

    # Nested brackets -> true
    assert is_valid("{[()]}") == True, "Nested brackets case failed"

    # Interleaved brackets -> true
    assert is_valid("([{}])") == True, "Interleaved brackets case failed"

    # Mismatched brackets -> false
    assert is_valid("(]") == False, "Mismatched brackets case failed"

    # Incorrect closing order -> false
    assert is_valid("([)]") == False, "Incorrect closing order case failed"

    # Extra closing bracket -> false
    assert is_valid("()[]}") == False, "Extra closing bracket case failed"

    # Extra opening bracket -> false
    assert is_valid("(){[") == False, "Extra opening bracket case failed"

    # Complex valid case
    assert is_valid("({[()]}{()[]})") == True, "Complex valid case failed"

    # Complex invalid case
    assert is_valid("({[()])}{()[]})") == False, "Complex invalid case failed"

    # Long repeated pattern -> true
    assert is_valid("([])([])([])([])") == True, "Long repeated pattern case failed"

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing valid parentheses implementation")
    test_is_valid()
