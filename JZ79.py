from typing import Tuple


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
    def IsBalanced_Solution(self, pRoot: TreeNode) -> bool:

        def bottomUp(node: TreeNode) -> Tuple[bool, int]:
            if node is None:
                return True, 0
            l, lh = bottomUp(node.left)
            r, rh = bottomUp(node.right)
            if not l or not r:
                return False, 0
            if abs(lh - rh) > 1:
                return False, 0
            else:
                return True, max(lh, rh) + 1

        flag, h = bottomUp(pRoot)
        return flag
