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
# @param p int整型
# @param q int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: int, q: int) -> int:
        if p > q:
            p, q = q, p

        def topDown(node: TreeNode, val1: int, val2: int) -> int:
            if val1 <= node.val <= val2:
                return node.val
            elif node.val < val1:
                return topDown(node.right, val1, val2)
            elif node.val > val2:
                return topDown(node.left, val1, val2)

        return topDown(root, p, q)
