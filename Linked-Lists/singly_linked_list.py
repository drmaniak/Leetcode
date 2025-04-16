class Node:
    def __init__(self, val: int):
        self.val = val
        self.next = None


class MyLinkedList:
    def __init__(self):
        self.head = Node(
            -9999
        )  # Initialize self.head to a dummy node to help with removal
        self.tail = self.head
        self.size = 0

    def get(self, index: int) -> int:
        curr = self.head.next  # Start from first non-dummy node
        count = 0

        # Loop till we reach an empty node
        while curr:
            # If node is at index, then return its value
            if count == index:
                return curr.val

            # Make next node as curr & increment count
            curr = curr.next
            count += 1

        # Return -1 if index out of bounds
        return -1

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)  # Create new node
        new_node.next = self.head.next  # Make its next node the old head node
        self.head.next = new_node  # type: ignore
        if not new_node.next:
            self.tail = new_node

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        self.tail.next = new_node  # type: ignore
        self.tail = new_node

    def addAtIndex(self, index: int, val: int) -> None:
        curr = self.head  # Start at dummy node
        count = 0
        new_node = Node(val)
        while count < index and curr:
            curr = curr.next
            count += 1

        # After the loop, curr.next is our targeted index

        if curr:
            new_node.next = curr.next
            curr.next = new_node  # type: ignore

            if not new_node.next:
                self.tail = new_node

    def deleteAtIndex(self, index: int) -> None:
        curr = self.head  # Start at dummy node
        count = 0

        while count < index and curr:
            curr = curr.next
            count += 1

        # After the loop, curr.next is our targeted index
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

    def getValues(self) -> list[int]:
        curr = self.head.next  # First non-dummy node
        values = []
        while curr:
            values.append(curr.val)
            curr = curr.next

        return values


def test_linked_list_operations():
    ll = MyLinkedList()

    # Test 1: Add at head
    ll.addAtHead(10)
    assert ll.get(0) == 10

    # Test 2: Add at tail
    ll.addAtTail(20)
    assert ll.get(1) == 20

    # Test 3: Add at index 1
    ll.addAtIndex(1, 15)
    assert ll.get(0) == 10
    assert ll.get(1) == 15
    assert ll.get(2) == 20

    # Test 4: Invalid get
    assert ll.get(-1) == -1
    assert ll.get(3) == -1

    # Test 5: Delete middle
    ll.deleteAtIndex(1)
    assert ll.get(0) == 10
    assert ll.get(1) == 20
    assert ll.get(2) == -1

    # Test 6: Delete head
    ll.deleteAtIndex(0)
    assert ll.get(0) == 20

    # Test 7: Delete tail
    ll.deleteAtIndex(0)
    assert ll.get(0) == -1

    # Test 8: Add after clearing list
    ll.addAtHead(100)
    ll.addAtTail(200)
    ll.addAtIndex(1, 150)
    assert ll.get(0) == 100
    assert ll.get(1) == 150
    assert ll.get(2) == 200

    # Test 9: Out-of-bounds addAtIndex (should do nothing)
    ll.addAtIndex(10, 300)
    assert ll.get(3) == -1

    # Test 10: Delete at invalid index
    ll.deleteAtIndex(5)  # Should do nothing
    assert ll.get(0) == 100
    assert ll.get(1) == 150
    assert ll.get(2) == 200

    print("✅ All linked list test cases passed.")


def test_extended_linked_list_cases():
    ll = MyLinkedList()

    # Test appending multiple and deleting tail
    for i in range(5):
        ll.addAtTail(i)  # List: 0 → 1 → 2 → 3 → 4

    assert ll.getValues() == [0, 1, 2, 3, 4]
    ll.deleteAtIndex(4)  # Remove tail
    assert ll.getValues() == [0, 1, 2, 3]
    assert ll.tail.val == 3

    # Add after deleting tail
    ll.addAtTail(99)
    assert ll.getValues() == [0, 1, 2, 3, 99]
    assert ll.tail.val == 99

    # Add at head repeatedly
    for v in [7, 8, 9]:
        ll.addAtHead(v)
    # List is now: 9 → 8 → 7 → 0 → 1 → 2 → 3 → 99
    assert ll.getValues() == [9, 8, 7, 0, 1, 2, 3, 99]

    # Delete middle element
    ll.deleteAtIndex(3)  # Removes 0
    assert ll.getValues() == [9, 8, 7, 1, 2, 3, 99]

    # Delete new head
    ll.deleteAtIndex(0)
    assert ll.getValues() == [8, 7, 1, 2, 3, 99]

    # Delete last element (tail)
    ll.deleteAtIndex(5)
    assert ll.tail.val == 3
    assert ll.getValues() == [8, 7, 1, 2, 3]

    # Insert back at index 5 (new tail)
    ll.addAtIndex(5, 42)
    assert ll.getValues() == [8, 7, 1, 2, 3, 42]
    assert ll.tail.val == 42

    # Try to delete out-of-bounds again
    ll.deleteAtIndex(10)  # should do nothing
    assert ll.getValues() == [8, 7, 1, 2, 3, 42]

    print("✅ All extended linked list tests passed.")


if __name__ == "__main__":
    test_linked_list_operations()
    test_extended_linked_list_cases()
