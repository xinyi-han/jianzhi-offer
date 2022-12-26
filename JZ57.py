from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @param sum int整型
# @return int整型一维数组
#
class Solution:
    def FindNumbersWithSum(self, array: List[int], sum: int) -> List[int]:
        i = 0
        j = len(array) - 1
        while i < j:
            total = array[i] + array[j]
            if total == sum:
                return [array[i], array[j]]
            elif total < sum:
                i += 1
            else:
                j -= 1
        return []
