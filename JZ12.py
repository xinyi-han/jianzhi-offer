from typing import List


class Solution:
    def hasPath(self, matrix: List[List[str]], word: str) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        pos = set()

        def backtrack(x: int, y: int) -> bool:
            if len(pos) == len(word):
                return True
            if not 0 <= x < m or not 0 <= y < n:
                return False
            elif (x, y) in pos:
                return False
            elif matrix[x][y] != word[len(pos)]:
                return False
            pos.add((x, y))
            if backtrack(x - 1, y):
                return True
            if backtrack(x + 1, y):
                return True
            if backtrack(x, y - 1):
                return True
            if backtrack(x, y + 1):
                return True
            pos.remove((x, y))
            return False

        for i in range(m):
            for j in range(n):
                if backtrack(i, j):
                    return True
        return False
