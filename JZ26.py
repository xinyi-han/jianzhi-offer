class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pRoot1 TreeNode类
# @param pRoot2 TreeNode类
# @return bool布尔型
#
class Solution:
    def HasSubtree(self, pRoot1: TreeNode, pRoot2: TreeNode) -> bool:
        if pRoot1 is None or pRoot2 is None:
            return False

        def isSubtree(node1: TreeNode, node2: TreeNode) -> bool:
            if node2 is None:
                return True
            if node1 is None:
                return False
            l = isSubtree(node1.left, node2.left)
            r = isSubtree(node1.right, node2.right)
            return l and r and node1.val == node2.val

        stack = list()
        stack.append(pRoot1)
        while len(stack) > 0:
            node = stack.pop()
            if node.left is not None:
                stack.append(node.left)
            if node.right is not None:
                stack.append(node.right)
            if node.val == pRoot2.val:
                if isSubtree(node, pRoot2):
                    return True
        return False
