from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pushV int整型一维数组
# @param popV int整型一维数组
# @return bool布尔型
#
class Solution:
    def IsPopOrder(self , pushV: List[int], popV: List[int]) -> bool:
        i = 0
        j = 0
        stack = list()
        while i < len(pushV):
            stack.append(pushV[i])
            while len(stack) > 0 and stack[-1] == popV[j]:
                stack.pop()
                j += 1
            if j == len(popV):
                return True
            i += 1
        return False
