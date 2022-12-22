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
# @param pre int整型一维数组
# @param vin int整型一维数组
# @return TreeNode类
#
class Solution:
    def reConstructBinaryTree(self, pre: List[int], vin: List[int]) -> TreeNode:
        if len(pre) == 0:
            return None
        val = pre[0]
        root = TreeNode(val)
        i = vin.index(val)
        root.left = self.reConstructBinaryTree(pre[1:i+1], vin[:i])
        root.right = self.reConstructBinaryTree(pre[i+1:], vin[i+1:])
        return root
