import math


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def cutRope(self, number: int) -> int:
        if number == 2: # (1, 1)
            return 1
        elif number == 3: # (2, 1)
            return 2
        ropes = list()
        mod = number % 3
        div = number // 3
        if mod == 0:
            ropes += [3] * div
        elif mod == 2:
            ropes += [3] * div + [2]
        elif mod == 1:
            ropes += [3] * (div - 1) + [2] * 2
        return math.prod(ropes)
