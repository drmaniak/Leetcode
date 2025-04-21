class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack: list[tuple[int, int]] = []

    def push(self, val: int) -> None:
        # Check if stack is empty or not
        if self.stack:
            # Compare incoming value against stack_max
            stack_max = self.max_stack[-1][0]
            max_val = val if val >= stack_max else None
            if max_val:
                self.max_stack.append((val, len(self.stack)))
        else:
            self.max_stack.append((val, 0))

        self.stack.append(val)

        # I need to add to the top of the stack

    def pop(self) -> int:
        # If the last element is the same as the max
        if self.max_stack[-1][1] == len(self.stack) - 1:
            # Remove the topmost max element
            self.max_stack.pop()

        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1][0]

    def popMax(self) -> int:
        max_val, max_idx = self.max_stack.pop()

        return self.stack.pop(max_idx)

    def __str__(self) -> str:
        return f"Stack: {self.stack}\n\nMax stack: {self.max_stack}"


def test_max_stack():
    s = MaxStack()
    s.push(5)
    s.push(1)
    s.push(5)
    print("After Pushing 5, 1, 5\n", s)
    assert s.top() == 5
    assert s.popMax() == 5  # removes top-most 5
    print("After popping max \n", s)
    assert s.top() == 1
    assert s.peekMax() == 5
    print("After peeking max \n", s)
    assert s.pop() == 1
    assert s.top() == 5
    print("✅ Passed basic test")


if __name__ == "__main__":
    test_max_stack()
