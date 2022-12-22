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
# @param root TreeNode类
# @param target int整型
# @return int整型二维数组
#
class Solution:
    def FindPath(self, root: TreeNode, target: int) -> List[List[int]]:
        output = list()

        def topDown(node: TreeNode, stack: List[int], sum: int):
            if node.left is None and node.right is None:
                if sum == target:
                    output.append(list(stack))
                return
            if node.left is None:
                topDown(node.right, list(stack) + [node.right.val], sum + node.right.val)
            elif node.right is None:
                topDown(node.left, list(stack) + [node.left.val], sum + node.left.val)
            else:
                topDown(node.right, list(stack) + [node.right.val], sum + node.right.val)
                topDown(node.left, list(stack) + [node.left.val], sum + node.left.val)

        if root is None:
            return output
        topDown(root, [root.val], root.val)
        return output
