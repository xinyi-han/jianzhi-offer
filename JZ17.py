from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型 最大位数
# @return int整型一维数组
#
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return list(range(1, 10 ** n))
