from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型
#
class Solution:
    def FindGreatestSumOfSubArray(self, array: List[int]) -> int:
        maxSum = array[0]
        sum = 0
        for num in array:
            if num + sum <= num:
                sum = num
            else:
                sum += num
            maxSum = max(maxSum, sum)
        return maxSum
