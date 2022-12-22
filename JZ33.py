from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param sequence int整型一维数组
# @return bool布尔型
#
class Solution:
    def VerifySquenceOfBST(self, sequence: List[int]) -> bool:

        def isValid(vals: List[int]) -> bool:
            if len(vals) == 0 or len(vals) == 1:
                return True
            pivot = len(vals) - 1
            for i, val in enumerate(vals[:-1]):
                if val > vals[-1]:
                    pivot = i
                    break
            if not all(list(map(lambda x: x > vals[-1], vals[pivot:-1]))):
                return False
            l = isValid(vals[:pivot])
            r = isValid(vals[pivot:-1])
            return l and r

        if len(sequence) == 0:
            return False
        return isValid(sequence)
