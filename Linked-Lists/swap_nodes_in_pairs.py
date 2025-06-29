# 🧩 Problem: Swap Nodes in Pairs
#
# 🤔 Difficulty: Medium
#
# 🔗 Link: https://leetcode.com/problems/swap-nodes-in-pairs
#
#     Given a linked list, swap every two adjacent nodes and return its head.
#     You must solve the problem without modifying the values in the list's nodes
#     (i.e., only nodes themselves may be changed.)
#
#     Example 1:
#     Input: head = [1,2,3,4]
#     Output: [2,1,4,3]
#
#     Example 2:
#     Input: head = []
#     Output: []
#
#     Example 3:
#     Input: head = [1]
#     Output: [1]
#
#     Example 4:
#     Input: head = [1,2,3]
#     Output: [2,1,3]
#
# ✅ Constraints:
#     - The number of nodes in the list is in the range [0, 100].
#     - 0 <= Node.val <= 100

from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __eq__(self, other: Optional["ListNode"]) -> bool:  # type: ignore
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


def swap_pairs_iterative(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Swap every two adjacent nodes in the linked list using iteration.

    Args:
        head: The head of the singly linked list

    Returns:
        The new head of the list after swapping every two nodes
    """
    # Your solution here

    # Create a dummy node
    dummy = ListNode(-69420, head)

    # Create pointers
    prev, curr = dummy, head

    while curr and curr.next:
        # Look ahead
        nxtPair = curr.next.next
        second = curr.next

        # Swap positions
        second.next = curr
        curr.next = nxtPair
        prev.next = second

        # Update pointers
        prev = curr
        curr = nxtPair

    return dummy.next


def swap_pairs_recursive(head: Optional[ListNode]) -> Optional[ListNode]:
    """
    Swap every two adjacent nodes in the linked list using recursion.

    Args:
        head: The head of the singly linked list

    Returns:
        The new head of the list after swapping every two nodes
    """
    # Your solution here

    if not head or not head.next:
        return head

    curr = head
    nxt = head.next

    swapped_list = swap_pairs_recursive(nxt.next)

    curr.next = swapped_list

    nxt.next = curr

    return nxt


# ✅ Test suite
def test_swap_nodes_in_pairs():
    # Helper to build linked list from Python list
    def build_linked_list(values: list[int]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        for val in values:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    test_cases = [
        ([], []),
        ([1], [1]),
        ([1, 2], [2, 1]),
        ([1, 2, 3], [2, 1, 3]),
        ([1, 2, 3, 4], [2, 1, 4, 3]),
        ([10, 20, 30, 40, 50], [20, 10, 40, 30, 50]),
    ]

    for i, (input_list, expected_list) in enumerate(test_cases):
        original = build_linked_list(input_list)
        expected = build_linked_list(expected_list)

        # Test iterative version
        result_iter = swap_pairs_iterative(build_linked_list(input_list))
        assert result_iter == expected, (
            f"[Iterative] Test case {i} failed: expected {expected}, got {result_iter}"
        )

        # Test recursive version
        result_rec = swap_pairs_recursive(build_linked_list(input_list))
        assert result_rec == expected, (
            f"[Recursive] Test case {i} failed: expected {expected}, got {result_rec}"
        )

    print("✅ All test cases passed for both iterative and recursive versions!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing swap nodes in pairs implementations")
    test_swap_nodes_in_pairs()
