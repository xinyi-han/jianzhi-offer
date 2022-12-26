from typing import List
from functools import cmp_to_key


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return string字符串
#
class Solution:
    def PrintMinNumber(self, numbers: List[int]) -> str:

        def cmp(s1: str, s2: str) -> int:
            if s1 + s2 < s2 + s1:
                return -1
            elif s1 + s2 > s2 + s1:
                return 1
            else:
                return 0

        numbers = list(map(str, numbers))
        numbers = sorted(numbers, key=cmp_to_key(cmp))
        return "".join(numbers)
