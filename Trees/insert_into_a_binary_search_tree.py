# 🧩 Problem: Insert into a Binary Search Tree
#
# 🤔 Difficulty: Medium
#
# 🔗 Link: https://leetcode.com/problems/insert-into-a-binary-search-tree
#
#   You are given the root node of a binary search tree (BST) and a value to insert into the tree.
#   Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
#
#   Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion.
#   You can return any of them.
#
#   Example 1:
#       Input:  root = [4,2,7,1,3], val = 5
#       Output: [4,2,7,1,3,5]
#
#   Example 2:
#       Input:  root = [40,20,60,10,30,50,70], val = 25
#       Output: [40,20,60,10,30,50,70,null,null,25]
#
#   Example 3:
#       Input:  root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
#       Output: [4,2,7,1,3,5]
#
# ✅ Constraints:
#     - The number of nodes in the tree will be in the range [0, 10^4].
#     - -10^8 <= Node.val <= 10^8
#     - All the values of the tree are unique.
#     - -10^8 <= val <= 10^8
#     - It is guaranteed that val does not exist in the original BST.

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(
        self,
        val: int = 0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(self, other: Optional["TreeNode"]) -> bool:  # type: ignore
        if not other:
            return False
        return (
            self.val == other.val
            and self.left == other.left
            and self.right == other.right
        )

    def __repr__(self):
        return f"TreeNode({self.val})"


def insert_into_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Insert a value into a BST and return the root of the tree after insertion.

    Args:
        root: Root of the binary search tree
        val: The value to insert into the BST

    Returns:
        The root of the updated BST
    """
    # Solve with Recursion #

    # Base case
    if not root:
        return TreeNode(val)

    # Recursively move down appropriate subtree
    if val > root.val:
        root.right = insert_into_bst(root.right, val)
    elif val < root.val:
        root.left = insert_into_bst(root.left, val)

    return root


# ✅ Test suite
def test_insert_into_bst():
    def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
        if not values:
            return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = deque(nodes[1:])
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.popleft()
                if kids:
                    node.right = kids.popleft()
        return nodes[0]

    def serialize(root: Optional[TreeNode]) -> List[int]:
        """Convert a BST back into level-order list (compact form)."""
        if not root:
            return []
        output = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                output.append(node.val)
                queue.append(node.left)  # type: ignore
                queue.append(node.right)  # type: ignore
            else:
                output.append(None)
        while output and output[-1] is None:
            output.pop()
        return output

    test_cases = [
        ([4, 2, 7, 1, 3], 5, [4, 2, 7, 1, 3, 5]),
        (
            [40, 20, 60, 10, 30, 50, 70],
            25,
            [40, 20, 60, 10, 30, 50, 70, None, None, 25],
        ),
        ([4, 2, 7, 1, 3, None, None, None, None, None, None], 5, [4, 2, 7, 1, 3, 5]),
        ([], 42, [42]),
        ([10], 5, [10, 5]),
        ([10], 15, [10, None, 15]),
    ]

    for i, (tree_vals, val, expected_vals) in enumerate(test_cases):
        root = build_tree(tree_vals)
        expected = build_tree(expected_vals)
        result = insert_into_bst(root, val)
        result_serialized = serialize(result)
        expected_serialized = serialize(expected)
        assert result_serialized == expected_serialized, (
            f"Test case {i} failed.\nInput tree: {tree_vals}, val: {val}"
            f"\nExpected: {expected_serialized}, Got: {result_serialized}"
        )

    print("✅ All test cases passed for insert_into_bst!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing insert_into_bst implementation")
    test_insert_into_bst()
