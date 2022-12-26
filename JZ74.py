from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sum int整型
# @return int整型二维数组
#
class Solution:
    def FindContinuousSequence(self, sum: int) -> List[List[int]]:
        output = list()
        if sum < 3:
            return output
        if sum % 2 == 0:
            nums = list(range(1, sum // 2 + 1))
        else:
            nums = list(range(1, sum // 2 + 2))
        i, j = 0, 0
        total = 0
        while j < len(nums):
            if total == sum:
                output.append(nums[i:j])
            if total <= sum:
                total += nums[j]
                j += 1
            elif total > sum:
                total -= nums[i]
                i += 1
        while total > sum:
            total -= nums[i]
            i += 1
        if total == sum:
            output.append(nums[i:j])
        return output
