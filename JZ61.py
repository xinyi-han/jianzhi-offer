from typing import List


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param numbers int整型一维数组
# @return bool布尔型
#
class Solution:
    def IsContinuous(self, numbers: List[int]) -> bool:
        numbers.sort()
        zero = 0
        for num in numbers:
            if num == 0:
                zero += 1
            elif num > 0:
                break
        if zero == 4:
            return True
        elif zero == 0:
            return set(numbers) == set(range(numbers[0], numbers[0] + 5))
        i = zero - 1
        j = len(numbers) - 2
        prev = numbers[-1]
        while j >= zero:
            if prev - numbers[j] == 1:
                j -= 1
            else:
                if i == -1:
                    return False
                numbers[i] = prev - 1
                i -= 1
            prev -= 1
        return True
