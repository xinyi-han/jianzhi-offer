import heapq


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param index int整型
# @return int整型
#
class Solution:
    def GetUglyNumber_Solution(self, index: int) -> int:
        heap = [1]
        heapq.heapify(heap)
        i = 0
        num = 0 # Edge case
        while i < index:
            num = heapq.heappop(heap)
            heapq.heappush(heap, num * 2)
            heapq.heappush(heap, num * 3)
            heapq.heappush(heap, num * 5)
            while heap[0] == num:
                heapq.heappop(heap)
            i += 1
        return num
