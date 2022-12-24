#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def Fibonacci(self, n: int) -> int:
        a, b = 0, 1
        i = 1
        num = 1
        while i < n:
            num = a + b
            if i % 2 == 1:
                a = num
            else:
                b = num
            i += 1
        return num
