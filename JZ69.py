#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param number int整型
# @return int整型
#
class Solution:
    def jumpFloor(self, number: int) -> int:
        cache = [1 for _ in range(number + 1)]
        for i in range(2, number + 1):
            cache[i] = cache[i - 2] + cache[i - 1]
        return cache[-1]
