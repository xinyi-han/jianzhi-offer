class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
#
# @param pHead1 ListNodeš▒╗
# @param pHead2 ListNodeš▒╗
# @return ListNodeš▒╗
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
