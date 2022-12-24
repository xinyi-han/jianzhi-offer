from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def duplicate(self, numbers: List[int]) -> int:
        digits = set()
        for num in numbers:
            if num in digits:
                return num
            digits.add(num)
        return -1
