from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param data int整型一维数组
# @return int整型
#
class Solution:
    def InversePairs(self, data: List[int]) -> int:
        self.pair = 0
        self.mergeSort(data)
        return self.pair % 1000000007

    def mergeSort(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums) // 2
        left = self.mergeSort(nums[:mid])
        right = self.mergeSort(nums[mid:])
        return self.merge(left, right)

    def merge(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        k = 0
        nums = list()
        while i < len(nums1) and j < len(nums2):
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i += 1
            else:
                nums.append(nums2[j])
                j += 1
                self.pair += len(nums1) - i
            k += 1
        if i == len(nums1):
            nums.extend(nums2[j:])
        else:
            nums.extend(nums1[i:])
        return nums
