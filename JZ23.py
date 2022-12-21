class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead: ListNode) -> ListNode:
        nodes = set()
        while pHead is not None:
            if pHead in nodes:
                return pHead
            nodes.add(pHead)
            pHead = pHead.next
        return None
