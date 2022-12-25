from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindNumsAppearOnce(self, array: List[int]) -> List[int]:
        hashSet = set()
        while len(array) > 0:
            num = array.pop()
            if num in hashSet:
                hashSet.remove(num)
            else:
                hashSet.add(num)
        output = list(hashSet)
        output.sort()
        return output
