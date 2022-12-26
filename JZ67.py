#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param s string字符串
# @return int整型
#
class Solution:
    def StrToInt(self, s: str) -> int:
        output = 0
        s = s.strip()
        if len(s) == 0:
            return output
        i = 0
        sign = 1
        if s[0] == "-":
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1
        while i < len(s):
            if not s[i].isdigit():
                break
            output *= 10
            output += int(s[i])
            if output >= 2**31:
                break
            i += 1
        output *= sign
        return max(-2**31, min(output, 2**31 - 1))
