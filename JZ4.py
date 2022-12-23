from typing import List, Tuple


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param target int整型
# @param array int整型二维数组
# @return bool布尔型
#
class Solution:
    def Find(self, target: int, array: List[List[int]]) -> bool:
        m = len(array)
        n = len(array[0])
        if m == 0 or n == 0: # Edge case: array = [[]]
            return False
        flagR, r = self.binarySearch(0, m - 1, [array[r][0] for r in range(m)], target)
        if flagR:
            return True
        elif r == 0:
            return False
        flagC, c = self.binarySearch(0, n - 1, array[r - 1], target)
        if flagC:
            return True
        elif c == n:
            return False
        array = [array[i][c:] for i in range(r)]
        return self.Find(target, array)

    def binarySearch(self, lo: int, hi: int, nums: List[int], target) -> Tuple[bool, int]:
        if lo > hi:
            return False, lo
        mid = (lo + hi) // 2
        if nums[mid] == target:
            return True, mid
        elif nums[mid] > target:
            return self.binarySearch(lo, mid - 1, nums, target)
        else:
            return self.binarySearch(mid + 1, hi, nums, target)
