from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param A int整型一维数组
# @return int整型一维数组
#
class Solution:
    def multiply(self, A: List[int]) -> List[int]:
        output = [1 for _ in A]
        for i, num in enumerate(A[:-1]):
            output[i+1] = output[i] * num
        prev = 1
        for j in range(len(A) - 1, 0, -1):
            prev *= A[j]
            output[j-1] *= prev
        return output
