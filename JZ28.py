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
# @return bool布尔型
#
class Solution:
    def isSymmetrical(self, pRoot: TreeNode) -> bool:

        def bottomUp(left: TreeNode, right: TreeNode) -> bool:
            if left is None and right is None:
                return True
            elif left is None or right is None:
                return False
            else:
                l = bottomUp(left.left, right.right)
                r = bottomUp(left.right, right.left)
                if not l or not r:
                    return False
                return left.val == right.val

        if pRoot is None:
            return True
        return bottomUp(pRoot.left, pRoot.right)
