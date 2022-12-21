class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead: RandomListNode) -> RandomListNode:
        hashMap = dict()  # key=old, value=new

        def bottomUp(node: RandomListNode) -> RandomListNode:
            if node is None:
                return None
            curr = RandomListNode(node.label)
            hashMap[node] = curr
            curr.next = bottomUp(node.next)
            if node.random is not None:
                curr.random = hashMap[node.random]
            return curr

        return bottomUp(pHead)
