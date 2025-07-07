# 🧩 Problem: Longest Substring Without Repeating Characters
#
# 🤔 Difficulty: Medium
#
# 🔗 Link: https://leetcode.com/problems/longest-substring-without-repeating-characters
#
#     Given a string s, find the length of the longest substring without duplicate characters.
#
#     A substring is a contiguous sequence of characters within a string.
#
#     Example 1:
#         Input:  "zxyzxyz"
#         Output: 3
#         Explanation: The string "xyz" is the longest without duplicate characters.
#
#     Example 2:
#         Input:  "xxxx"
#         Output: 1
#
# ✅ Constraints:
#     - 0 <= s.length <= 1000
#     - s may consist of printable ASCII characters.


def length_of_longest_substring(s: str) -> int:
    """
    Return the length of the longest substring without repeating characters.

    Args:
        s: Input string consisting of printable ASCII characters

    Returns:
        Length of the longest substring without duplicate characters
    """
    # Your solution here

    # This is a sliding window problem

    charset = set()
    longest = 0

    L = 0

    for R in range(len(s)):
        while s[R] in charset:
            charset.remove(s[L])
            L += 1

        charset.add(s[R])
        longest = max(longest, R - L + 1)

    return longest


# ✅ Test suite
def test_length_of_longest_substring():
    test_cases = [
        ("", 0),
        ("a", 1),
        ("abcabcbb", 3),  # "abc"
        ("bbbbb", 1),  # "b"
        ("pwwkew", 3),  # "wke"
        ("zxyzxyz", 3),  # "xyz"
        ("dvdf", 3),  # "vdf"
        ("abcdef", 6),  # all unique
        ("abba", 2),  # "ab"
        ("tmmzuxt", 5),  # "mzuxt"
        ("abcabcabcd", 4),  # "abcd"
    ]

    for i, (s, expected) in enumerate(test_cases):
        result = length_of_longest_substring(s)
        assert result == expected, (
            f"Test case {i} failed.\nInput: {s}\nExpected: {expected}\nGot: {result}"
        )

    print(
        "✅ All test cases passed for longest substring without repeating characters!"
    )


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing longest substring without repeating characters implementation")
    test_length_of_longest_substring()
