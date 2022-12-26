from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param matrix int整型二维数组
# @return int整型一维数组
#
class Solution:
    def printMatrix(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        output = list()
        round = min(m, n) // 2
        k = 0
        while k < round:
            for j in range(0 + k, n - 1 - k):
                output.append(matrix[0 + k][j])
            for i in range(0 + k, m - 1 - k):
                output.append(matrix[i][n - 1 - k])
            for j in range(n - 1 - k, 0 + k, -1):
                output.append(matrix[m - 1 - k][j])
            for i in range(m - 1 - k, 0 + k, -1):
                output.append(matrix[i][0 + k])
            k += 1
        if len(output) != m * n:
            rows = list(range(k, m - k))
            columns = list(range(k, n - k))
            for r in rows:
                for c in columns:
                    output.append(matrix[r][c])
        return output
