from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def reOrderArrayTwo(self, array: List[int]) -> List[int]:
        i = 0
        j = len(array) - 1
        while i < j:
            while i < j and array[i] % 2 == 1:
                i += 1
            while i < j and array[j] % 2 == 0:
                j -= 1
            if i >= j:
                break
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        return array
