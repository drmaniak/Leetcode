class MaxStack:
    def __init__(self):
        self.stack = []
        self.maxstack = []

    def push(self, val: int) -> None:
        # Check if stack is empty or not
        self.stack.append(val)

        if len(self.stack) == 1:
            self.maxstack.append(val)
        else:
            currmax = self.maxstack[-1]
            self.maxstack.append(max(currmax, val))

    def pop(self) -> int | None:
        if self.stack and self.maxstack:
            val = self.stack.pop()
            maxval = self.maxstack.pop()

            return val
        else:
            return None

    def top(self) -> int | None:
        if self.stack and self.maxstack:
            val = self.stack[-1]
            maxval = self.maxstack[-1]

            return val
        else:
            return None

    def peekMax(self) -> int | None:
        if self.stack and self.maxstack:
            val = self.stack[-1]
            maxval = self.maxstack[-1]

            return maxval
        else:
            return None

    def popMax(self) -> int | None:
        if self.stack and self.maxstack:
            val = self.stack.pop()
            maxval = self.maxstack.pop()

            return maxval
        else:
            return None

    def __str__(self) -> str:
        repr = f"Stack: {self.stack}\nMax Stack: {self.maxstack}"
        return repr


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
