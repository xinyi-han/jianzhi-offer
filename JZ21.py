from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def reOrderArray(self, array: List[int]) -> List[int]:
        stack = list()
        i = len(array) - 1
        for j in range(len(array) - 1, -1, -1):
            num = array[j]
            if num % 2 == 0:
                array[i] = num
                i -= 1
            else:
                stack.append(num)
        k = 0
        while len(stack) > 0:
            num = stack.pop()
            array[k] = num
            k += 1
        return array
