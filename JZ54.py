class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param proot TreeNode类
# @param k int整型
# @return int整型
#
class Solution:
    def KthNode(self, proot: TreeNode, k: int) -> int:
        if proot is None or k == 0:
            return -1
        vals = list()

        def inOrder(node: TreeNode):
            if node is None:
                return
            inOrder(node.left)
            vals.append(node.val)
            inOrder(node.right)

        inOrder(proot)
        if len(vals) < k:
            return -1
        return vals[k - 1]
