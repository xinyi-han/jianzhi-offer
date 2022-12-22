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
# @param sum int整型
# @return bool布尔型
#
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        def topDown(node: TreeNode, total: int) -> bool:
            l = False
            r = False
            if node.left is None and node.right is None:
                if total == sum:
                    return True
                return False
            elif node.left is None:
                r = topDown(node.right, total + node.right.val)
            elif node.right is None:
                l = topDown(node.left, total + node.left.val)
            else:
                r = topDown(node.right, total + node.right.val)
                l = topDown(node.left, total + node.left.val)
            return l or r

        if root is None:
            return False
        return topDown(root, root.val)
