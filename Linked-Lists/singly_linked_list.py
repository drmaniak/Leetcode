# 🧩 Problem: Design a Singly Linked List
#
# 🤔 Difficulty: Medium
#
# 🔗 Link:


class Node:
    def __init__(self, val: int):
        self.val = val
        self.next: Node | None = None


class MyLinkedList:
    def __init__(self):
        self.dummy = Node(val=-69420)
        self.tail: Node | None = None
        self.len = 0

    def get(self, index: int) -> int:
        # Initialize the pointer at the head node
        curr = self.dummy.next

        if (not curr) or (index < 0) or (index >= self.len):
            return -1

        # Initialize a counter variable
        count = 0

        # When the loop breaks, we are at our desired node
        while count < index and curr.next:
            curr = curr.next
            count += 1

        val = curr.val
        return val

    def addAtHead(self, val: int) -> None:
        # Store the current var that dummy.next points to
        nxt = self.dummy.next

        # Create new head_node
        new_head = Node(val)

        # Assign dummy.next to new_head
        self.dummy.next = new_head

        # Assign new_head.next to stored temp nxt
        new_head.next = nxt

        # If head is the only node
        if not nxt:
            self.tail = new_head

        # Increment len
        self.len += 1

    def addAtTail(self, val: int) -> None:
        curr = self.dummy

        # After loop, we arrive at last node
        while curr.next:
            curr = curr.next

        # Assign last node's next pointer to new node
        new_tail = Node(val)
        curr.next = new_tail

        # Update tail pointer
        self.tail = new_tail

        # Increment len
        self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:
        # Edge cases for adding at head or tail

        if index > self.len:
            return

        if index == 0:
            self.addAtHead(val)
            return

        if index == self.len:
            self.addAtTail(val)
            return

        # Initialize at dummy, since we need to re-assign pointers after adding
        curr = self.dummy

        count = 0

        # After breaking, we arrive at the node preceeding our target index
        while count < index and curr.next:
            curr = curr.next
            count += 1

        nxt = curr.next
        new_node = Node(val)
        curr.next = new_node
        new_node.next = nxt

        self.len += 1

    def deleteAtIndex(self, index: int) -> None:
        prev, curr = self.dummy, self.dummy.next

        if not curr:
            return

        if index > self.len:
            return

        count = 0

        # We need to also store a prev pointer
        while count < index and curr.next:
            prev = curr
            curr = curr.next  # when breaking, we are at our target index
            count += 1

        # we need to snip out the curr and connect prev to nxt
        nxt = curr.next
        prev.next = nxt

        # Update tail if at last node
        if not nxt:
            self.tail = prev

        # Update length
        self.len -= 1
        self.len = max(0, self.len)

    def getValues(self) -> list[int]:
        curr = self.dummy

        vals = []

        while curr.next:
            curr = curr.next
            vals.append(curr.val)

        return vals


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
