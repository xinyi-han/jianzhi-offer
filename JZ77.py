from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot TreeNode类
# @return int整型二维数组
#
class Solution:
    def Print(self, pRoot: TreeNode) -> List[List[int]]:
        output = list()
        stack = list()
        stack.append(pRoot)
        i = 0
        while len(stack) > 0:
            vals = list()
            level = list()
            if i % 2 == 0:
                while len(stack) > 0:
                    node = stack.pop()
                    if node is None:
                        continue
                    vals.append(node.val)
                    level.append(node.left)
                    level.append(node.right)
            else:
                while len(stack) > 0:
                    node = stack.pop()
                    if node is None:
                        continue
                    vals.append(node.val)
                    level.append(node.right)
                    level.append(node.left)
            stack = level
            if len(vals) > 0:
                output.append(vals)
            i += 1
        return output
