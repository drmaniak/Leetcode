# 🧩 Problem: Search in a Binary Search Tree
#
# 🤔 Difficulty: Easy
#
# 🔗 Link: https://leetcode.com/problems/search-in-a-binary-search-tree
#
#   You are given the root of a binary search tree (BST) and an integer `val`.
#
#   Find the node in the BST such that the node's value equals `val`, and return the subtree
#   rooted with that node. If such a node does not exist, return `None`.
#
#   Example 1:
#       Input:  root = [4,2,7,1,3], val = 2
#       Output: [2,1,3]
#
#   Example 2:
#       Input:  root = [4,2,7,1,3], val = 5
#       Output: []
#
# ✅ Constraints:
#     - The number of nodes in the tree is in the range [1, 5000].
#     - 1 <= Node.val <= 10^7
#     - `root` is a binary search tree.
#     - 1 <= val <= 10^7

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


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    """
    Search for a node with value `val` in a Binary Search Tree (BST).

    Args:
        root: The root of the BST
        val: The target value to search for

    Returns:
        The subtree rooted at the node with value `val`, or None if not found
    """
    # Your solution here

    if not root:
        return None

    if val > root.val:
        return search_bst(root.right, val)
    elif val < root.val:
        return search_bst(root.left, val)
    else:
        return root


# ✅ Test suite
def test_search_bst():
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
                queue.append(node.left)
                queue.append(node.right)
            else:
                output.append(None)
        while output and output[-1] is None:
            output.pop()
        return output

    test_cases = [
        ([4, 2, 7, 1, 3], 2, [2, 1, 3]),
        ([4, 2, 7, 1, 3], 5, []),
        ([4], 4, [4]),
        ([4], 2, []),
        ([5, 3, 8, 2, 4, 7, 9], 8, [8, 7, 9]),
        ([5, 3, 8, 2, 4, 7, 9], 3, [3, 2, 4]),
    ]

    for i, (tree_vals, val, expected_vals) in enumerate(test_cases):
        root = build_tree(tree_vals)
        expected = build_tree(expected_vals)
        result = search_bst(root, val)
        result_serialized = serialize(result)
        expected_serialized = serialize(expected)
        assert result_serialized == expected_serialized, (
            f"Test case {i} failed.\nInput tree: {tree_vals}, val: {val}"
            f"\nExpected: {expected_serialized}, Got: {result_serialized}"
        )

    print("✅ All test cases passed for search_bst!")


# 🧪 Run tests
if __name__ == "__main__":
    print("Testing search_bst implementation")
    test_search_bst()
