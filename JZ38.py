from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return string字符串一维数组
#
class Solution:
    def Permutation(self, str: str) -> List[str]:
        s = list(str)
        hashMap = dict()
        for char in s:
            hashMap[char] = hashMap.get(char, 0) + 1
        output = list()

        def backtrack(substring: str, chars: dict):
            if len(substring) == len(s):
                output.append(substring)
                return
            keys = [k for k, v in chars.items() if v != 0]
            for char in keys:
                copyMap = dict(chars)
                copyMap[char] -= 1
                backtrack(substring + char, copyMap)

        backtrack("", hashMap)
        return output
