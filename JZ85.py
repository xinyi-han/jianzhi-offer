from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param array int整型一维数组
# @return int整型一维数组
#
class Solution:
    def FindGreatestSumOfSubArray(self, array: List[int]) -> List[int]:
        i = 0
        l, r = 0, 0
        sum = 0
        maxSum = array[0]
        for j, num in enumerate(array):
            if num + sum < num:
                i = j
                sum = num
            else:
                sum += num
            if sum > maxSum:
                maxSum =sum
                l = i
                r = j
            elif sum == maxSum and j - i > r - l:
                l = i
                r = j
        return array[l:r+1]
