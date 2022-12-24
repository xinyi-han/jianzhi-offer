import math


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 解码
# @param nums string字符串 数字串
# @return int整型
#
class Solution:
    def solve(self, nums: str) -> int:
        substrings = list()
        substring = ""
        for num in nums:
            substring += num
            if int(num) > 2:
                substrings.append(substring)
                substring = ""
            elif num == "0":
                if len(substring) > 2:
                    substrings.append(substring[:-2])
                    substrings.append(substring[-2:])
                elif len(substring) == 2:
                    substrings.append(substring)
                else:
                    return 0
                substring = ""
        if len(substring) > 0:
            substrings.append(substring)

        def numOfWays(s: str) -> int:
            if len(s) == 1:
                return 1
            if len(s) == 2 and s[-1] == "0":
                return 1
            cache = [1 for _ in range(len(s) + 1)]
            for i in range(2, len(s) + 1):
                if int(s[i-2:i]) > 26:
                    cache[i] = cache[i-1]
                else:
                    cache[i] = cache[i-2] + cache[i-1]
            return cache[-1]

        ways = [numOfWays(s) for s in substrings]
        return math.prod(ways)
