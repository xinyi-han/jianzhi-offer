class Node:
    def __init__(self, val=0, minimum=0):
        self.val = val
        self.minimum = minimum


class Solution:
    def __init__(self):
        self.stack = list()

    def push(self, val: int):
        if len(self.stack) == 0:
            node = Node(val, val)
        else:
            node = Node(val, min(val, self.stack[-1].minimum))
        self.stack.append(node)

    def pop(self) -> int:
        return self.stack.pop().val

    def top(self) -> int:
        return self.stack[-1].val

    def min(self) -> int:
        return self.stack[-1].minimum
