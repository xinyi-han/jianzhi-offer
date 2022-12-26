#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param str string字符串
# @return int整型
#
class Solution:
    def FirstNotRepeatingChar(self, str: str) -> int:
        hashMap = dict()
        hashSet = set()
        for i, s in enumerate(str):
            if s in hashSet:
                continue
            elif s in hashMap:
                hashMap.pop(s)
                hashSet.add(s)
            else:
                hashMap[s] = i
        if len(hashMap) == 0:
            return -1
        pairs = [(v, k) for k, v in hashMap.items()]
        pairs.sort()
        return pairs[0][0]
