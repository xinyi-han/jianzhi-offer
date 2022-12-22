class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
#
# @param pRootOfTree TreeNode类
# @return TreeNode类
#
class Solution:
    def Convert(self, pRootOfTree: TreeNode) -> TreeNode:
        dummy = TreeNode(-1)

        def topDown(node: TreeNode, lowerB: TreeNode, upperB: TreeNode):
            if node.left is None and node.right is None:
                node.left = lowerB
                node.right = upperB
                if lowerB is None:
                    dummy.right = node
                else:
                    lowerB.right = node
                if upperB is not None:
                    upperB.left = node
            elif node.right is None:
                topDown(node.left, lowerB, node)
                node.right = upperB
            elif node.left is None:
                topDown(node.right, node, upperB)
                node.left = lowerB
                if lowerB is None: # Edge case: {1,#,2,#,3,#,4,#,5}
                    dummy.right = node
            else:
                topDown(node.left, lowerB, node)
                topDown(node.right, node, upperB)

        if pRootOfTree is None:
            return None
        topDown(pRootOfTree, None, None)
        return dummy.right
