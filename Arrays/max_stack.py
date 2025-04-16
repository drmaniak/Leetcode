class MaxStack:
    def __init__(self):
        self.stack = []
        self.max_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        # handle appending to max_stack
        if not self.max_stack:
            self.max_stack.append((val, 0))
        else:
            if val >= self.max_stack[-1][0]:
                self.max_stack.append((val, len(self.stack) - 1))

    def pop(self) -> int:
        if self.max_stack[-1][0] == self.stack[-1]:
            self.max_stack.pop()

        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return self.max_stack[-1][0]

    def popMax(self) -> int:
        maxval, maxidx = self.max_stack.pop()
        self.stack.pop(maxidx)
        return maxval

    def __str__(self) -> str:
        return f"Stack: {self.stack}\nMax Stack: {self.max_stack}"


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
