#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @return int整型
#
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n == 0:
            return 0
        i = 1
        num = 9
        while True:
            if n - num * i < 0:
                break
            n -= num * i
            num *= 10
            i += 1
        div = n // i
        mod = n % i
        if mod == 0:
            s = str(num // 9 + div - 1)
            return int(s[-1])
        else:
            s = str(num // 9 + div)
            return int(s[mod - 1])
