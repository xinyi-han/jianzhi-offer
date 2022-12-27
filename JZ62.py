from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param n int整型
# @param m int整型
# @return int整型
#
class Solution:
    def LastRemaining_Solution(self, n: int, m: int) -> int:

        def topDown(nums: List[int]) -> int:
            if len(nums) == 1:
                return nums[0]
            mod = m % len(nums)
            if mod == 0:
                return topDown(nums[:-1])
            else:
                return topDown(nums[mod:] + nums[:mod - 1])

        return topDown(list(range(n)))
