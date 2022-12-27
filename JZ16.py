import math


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param base double浮点型
# @param exponent int整型
# @return double浮点型
#
class Solution:
    def Power(self, base: float, exponent: int) -> float:
        if base == 0:
            return 0
        if exponent == 0:
            return 1
        sign = 1 if exponent > 0 else -1
        exponent = abs(exponent)
        exps = list()
        while exponent > 0:
            exp = int(math.log2(exponent))
            exps.append(exp)
            exponent -= 2**exp
        cache = {0: 1}

        def topDown(base: float, e: int, i: int):
            cache[i] = base
            if e == 0:
                return
            topDown(base * base, e - 1, i * 2)

        topDown(base, exps[0], 1)
        output = 1
        for exp in exps:
            output *= cache[2**exp]
        return output if sign == 1 else 1 / output
