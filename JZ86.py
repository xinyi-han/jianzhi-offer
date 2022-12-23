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
# @param o1 int整型
# @param o2 int整型
# @return int整型
#
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, o1: int, o2: int) -> int:
        self.ancestor = None

        def bottomUp(node: TreeNode, val1: int, val2: int) -> bool:
            if node is None or self.ancestor is not None:
                return False
            l = bottomUp(node.left, val1, val2)
            r = bottomUp(node.right, val1, val2)
            if l and r:
                self.ancestor = node
                return False
            elif not l and not r:
                return node.val == val1 or node.val == val2
            elif l or r:
                if node.val == val1 or node.val == val2:
                    self.ancestor = node
                    return False
                return True

        bottomUp(root, o1, o2)
        return self.ancestor.val
