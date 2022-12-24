#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param threshold int整型
# @param rows int整型
# @param cols int整型
# @return int整型
#
class Solution:
    def movingCount(self, threshold: int, rows: int, cols: int) -> int:
        pos = set()
        ban = set()

        def backtrack(i: int, j: int):
            if not 0 <= i < rows or not 0 <= j < cols:
                return
            if (i, j) in pos or (i, j) in ban:
                return
            if sum(list(map(int, list(str(i) + str(j))))) > threshold:
                ban.add((i, j))
                return
            pos.add((i, j))
            backtrack(i - 1, j)
            backtrack(i + 1, j)
            backtrack(i, j - 1)
            backtrack(i, j + 1)

        backtrack(0, 0)
        return len(pos)
