from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return int整型
#
class Solution:
    def MoreThanHalfNum_Solution(self, numbers: List[int]) -> int:
        cache = dict()
        for num in numbers:
            for n in cache:
                if n != num:
                    cache[n] -= 1
                    if cache[n] == 0:
                        cache.pop(n)
                    break
            else:
                cache[num] = cache.get(num, 0) + 1
        return list(cache.keys())[0]
