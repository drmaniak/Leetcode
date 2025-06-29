# 🧩 Problem: Valid Palindrome
#
# 🤔 Difficulty: Easy
#
# 🔗 Link: https://leetcode.com/problems/valid-palindrome
#
#     Given a string s, return true if it is a palindrome, otherwise return false.
#
#     A palindrome is a string that reads the same forward and backward. It is also case-insensitive
#     and ignores all non-alphanumeric characters.
#
#     Note: Alphanumeric characters consist of letters (A-Z, a-z) and numbers (0-9).

# ✅ Constraints
#
#     1 <= s.length <= 1000
#     s is made up of only printable ASCII characters.


def is_palindrome(s: str) -> bool:
    """
    Determines if a string is a palindrome, ignoring case and non-alphanumeric characters.

    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(n) for creating the filtered string

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """

    valid_string = "".join([char.lower() for char in s if char.isalnum()])

    return valid_string == valid_string[::-1]


# Two-pointer approach with O(1) space complexity
def is_palindrome_two_pointers(s: str) -> bool:
    """
    Determines if a string is a palindrome using the two-pointer approach.

    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) as we only use pointers

    Args:
        s: Input string

    Returns:
        True if the string is a palindrome, False otherwise
    """

    n = len(s)

    if n == 1:
        return True

    L = 0
    R = n - 1

    while L < R:
        # Iterate through L and R until we arrive at valid characters
        while L < R and not s[L].isalnum():
            L += 1

        while L < R and not s[R].isalnum():
            R -= 1

        charL = s[L].lower()
        charR = s[R].lower()

        if charL != charR:
            return False
        else:
            L += 1
            R -= 1

    return True


# ✅ Thorough test suite
def test_is_palindrome():
    # Example 1: "Was it a car or a cat I saw?"
    assert is_palindrome("Was it a car or a cat I saw?") == True
    assert is_palindrome_two_pointers("Was it a car or a cat I saw?") == True

    # Example 2: "tab a cat"
    assert is_palindrome("tab a cat") == False
    assert is_palindrome_two_pointers("tab a cat") == False

    # Empty string (technically a palindrome)
    assert is_palindrome("") == True
    assert is_palindrome_two_pointers("") == True

    # Single character
    assert is_palindrome("a") == True
    assert is_palindrome_two_pointers("a") == True

    # Palindrome with numbers
    assert is_palindrome("A man, a plan, a canal: Panama") == True
    assert is_palindrome_two_pointers("A man, a plan, a canal: Panama") == True

    # Palindrome with special characters
    assert is_palindrome("Race a car") == False
    assert is_palindrome_two_pointers("Race a car") == False

    # Palindrome with mixed case
    assert is_palindrome("No 'x' in Nixon") == True
    assert is_palindrome_two_pointers("No 'x' in Nixon") == True

    # String with only special characters
    assert is_palindrome(".,;:") == True
    assert is_palindrome_two_pointers(".,;:") == True

    # String with numbers
    assert is_palindrome("12321") == True
    assert is_palindrome_two_pointers("12321") == True

    # String with mixed alphanumeric characters
    assert is_palindrome("a1b2c3c2b1a") == True
    assert is_palindrome_two_pointers("a1b2c3c2b1a") == True

    print("✅ All test cases passed!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing valid palindrome implementations")
    test_is_palindrome()
