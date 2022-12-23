class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node: int):
        self.stack1.append(node)

    def pop(self) -> int:
        if len(self.stack2) > 0:
            return self.stack2.pop()
        while len(self.stack1) > 0:
            node = self.stack1.pop()
            self.stack2.append(node)
        return self.stack2.pop()
