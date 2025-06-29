# 🧩 Problem: Reverse Linked List
#
# 🤔 Difficulty: Easy
#
# 🔗 Link: https://leetcode.com/problems/reverse-linked-list/
#
#     Given the head of a singly linked list, reverse the list, and return the reversed list.
#
#     Example 1:
#     Input: head = [1,2,3,4,5]
#     Output: [5,4,3,2,1]
#
#     Example 2:
#     Input: head = [1,2]
#     Output: [2,1]
#
#     Example 3:
#     Input: head = []
#     Output: []
#
# ✅ Constraints
#
#     - The number of nodes in the list is the range [0, 5000].
#     - -5000 <= Node.val <= 5000


from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __eq__(self, other: Optional["ListNode"]) -> bool:
        """Helper to compare two linked lists."""
        curr1, curr2 = self, other
        while curr1 and curr2:
            if curr1.val != curr2.val:
                return False
            curr1, curr2 = curr1.next, curr2.next
        return curr1 is None and curr2 is None

    def __repr__(self):
        values = []
        curr = self
        while curr:
            values.append(str(curr.val))
            curr = curr.next
        return "->".join(values)


def reverse_list_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list using iteration.

    Args:
        head: The head node of the linked list

    Returns:
        The new head of the reversed linked list
    """
    # Your solution here
    if not head:
        return

    prev, curr = None, head

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr

        curr = tmp

    return prev


def reverse_list_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Reverse a singly linked list using recursion.

    Args:
        head: The head node of the linked list

    Returns:
        The new head of the reversed linked list
    """
    # Your solution here

    # Edge case
    if not head:
        return

    # Base case for recursion (returning the last element as the new head)
    if not head.next:
        return head

    new_head = reverse_list_recursive(head.next)

    # Flipping the links
    # 4->5->None becomes 5 -> 4 -> None
    head.next.next = head
    head.next = None

    return new_head


# ✅ Test suite
def test_reverse_linked_list():
    # Helper to build linked list from Python list
    def build_linked_list(values: list[int]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    # Helper to convert linked list to Python list
    def linked_list_to_list(head: Optional[ListNode]) -> list[int]:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
    ]

    for i, (input_list, expected_list) in enumerate(test_cases):
        original = build_linked_list(input_list)
        expected = build_linked_list(expected_list)

        # Test iterative version
        result_iter = reverse_list_iterative(build_linked_list(input_list))
        assert result_iter == expected, (
            f"[Iterative] Test case {i} failed: expected {expected}, got {result_iter}"
        )

        # Test recursive version
        result_rec = reverse_list_recursive(build_linked_list(input_list))
        assert result_rec == expected, (
            f"[Recursive] Test case {i} failed: expected {expected}, got {result_rec}"
        )

    print("✅ All test cases passed for both iterative and recursive versions!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing reverse linked list implementations")
    test_reverse_linked_list()
