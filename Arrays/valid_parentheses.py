# Problem Summary: (LeetCode #20 — Valid Parentheses)
#
#     Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.
#
#     A string is valid if:
#
#         Open brackets are closed by the same type of brackets.
#
#         Open brackets are closed in the correct order.


def is_valid(s: str) -> bool:
    """
    Implement this function to return True if the parentheses in the string are valid.
    Valid means:
    - Every opening bracket has a corresponding closing bracket of the same type.
    - Brackets are closed in the correct order.
    """
    # 🔧 Your implementation goes here

    # Create stack to hold openinig pairs
    stack = []

    # Handle edge case with odd len(s)
    if len(s) % 2 != 0:
        return False

    # Create lookup for close-pairs
    close_pairs = {
        ")": "(",
        "}": "{",
        "]": "[",
    }

    # Iterate through chars in s
    for char in s:
        # Handle open pairs
        if char not in close_pairs:
            stack.append(char)  # Add open pairs to stack
        else:
            # if stack is empty
            if not stack:
                return False

            # Try to match close+opening pairs
            val = close_pairs[char]
            last_val = stack.pop()
            if val != last_val:
                return False

    return not stack


def test_is_valid():
    # ✅ Basic valid cases
    assert is_valid("()")
    assert is_valid("[]")
    assert is_valid("{}")
    assert is_valid("()[]{}")
    assert is_valid("{[()]}")
    assert is_valid("({[]})")
    assert is_valid("((()))")
    assert is_valid("{[({[()]})]}")

    # ❌ Invalid: mismatched types
    assert not is_valid("(]")
    assert not is_valid("([)]")
    assert not is_valid("{(})")
    assert not is_valid("{[}")

    # ❌ Invalid: incorrect order
    assert not is_valid(")(")
    assert not is_valid("[(])")
    assert not is_valid("({)}")

    # ❌ Invalid: missing closing
    assert not is_valid("(")
    assert not is_valid("[")
    assert not is_valid("{")
    assert not is_valid("(((")

    # ❌ Invalid: extra closing
    assert not is_valid(")")
    assert not is_valid("]")
    assert not is_valid("}")
    assert not is_valid("()))")

    # ✅ Edge case: empty string is valid
    assert is_valid("")

    # ✅ Valid with long balanced mix
    assert is_valid("[]{}(){{[[(())]]}}")

    # ❌ Invalid with imbalance deep in nesting
    assert not is_valid("{[(())]]}")

    print("✅ All ruff-compliant test cases passed!")


if __name__ == "__main__":
    test_is_valid()
