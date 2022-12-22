class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    def GetNext(self, pNode: TreeLinkNode) -> TreeLinkNode:
        if pNode.right is None:
            while pNode.next is not None and pNode == pNode.next.right:
                pNode = pNode.next
            return pNode.next
        else:
            node = pNode.right
            while node.left is not None:
                node = node.left
            return node
