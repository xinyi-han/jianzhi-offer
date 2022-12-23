from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @param k int整型
# @return int整型
#
class Solution:
    def GetNumberOfK(self, data: List[int], k: int) -> int:
        def binarySearch(lo: int, hi: int, nums: List[int], target: int) -> int:
            if lo > hi:
                return -1
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binarySearch(lo, mid - 1, nums, target)
            else:
                return binarySearch(mid + 1, hi, nums, target)

        i = binarySearch(0, len(data) - 1, data, k)
        if i == -1:
            return 0
        l, r = i, i
        while True:
            j = binarySearch(0, l - 1, data, k)
            if j == -1:
                break
            l = j
        while True:
            j = binarySearch(r + 1, len(data) - 1, data, k)
            if j == -1:
                break
            r = j
        return r - l + 1
