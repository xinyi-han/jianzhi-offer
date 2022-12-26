#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @param n int整型
# @return string字符串
#
class Solution:
    def LeftRotateString(self, str: str, n: int) -> str:
        if len(str) == 0:
            return ""
        n = n % len(str)
        return str[n:] + str[:n]
