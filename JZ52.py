class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        nodes = set()
        while pHead1 is not None:
            nodes.add(pHead1)
            pHead1 = pHead1.next
        while pHead2 is not None:
            if pHead2 in nodes:
                return pHead2
            pHead2 = pHead2.next
        return None
