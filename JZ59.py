from typing import List
from collections import deque


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param num int整型一维数组
# @param size int整型
# @return int整型一维数组
#
class Solution:
    def maxInWindows(self, num: List[int], size: int) -> List[int]:
        output = list()
        if size == 0 or size > len(num):
            return output
        queue = deque()
        for i in range(size):
            if len(queue) == 0:
                queue.append((num[i], i))
            elif num[i] < queue[-1][0]:
                queue.append((num[i], i))
            else:
                while len(queue) > 0 and queue[-1][0] <= num[i]:
                    queue.pop()
                queue.append((num[i], i))
        i = size
        while i < len(num):
            output.append(queue[0][0])
            if i - queue[0][1] == size:
                queue.popleft()
            while len(queue) > 0 and queue[-1][0] <= num[i]:
                queue.pop()
            queue.append((num[i], i))
            i += 1
        output.append(queue[0][0])
        return output
