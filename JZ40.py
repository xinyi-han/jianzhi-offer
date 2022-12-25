from typing import List
import heapq


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param input int整型一维数组
# @param k int整型
# @return int整型一维数组
#
class Solution:
    def GetLeastNumbers_Solution(self, input: List[int], k: int) -> List[int]:
        # (priority, index, num)
        heap = [(num, i, num) for i, num in enumerate(input)]
        heapq.heapify(heap)
        output = list()
        i = 0
        while i < k:
            _, _, num = heapq.heappop(heap)
            output.append(num)
            i += 1
        return output
