class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead1 ListNode类
# @param pHead2 ListNode类
# @return ListNode类
#
class Solution:
    def Merge(self, pHead1: ListNode, pHead2: ListNode) -> ListNode:
        if pHead1 is None and pHead2 is None:
            return None
        dummy = ListNode(0)
        node = dummy
        while pHead1 is not None and pHead2 is not None:
            if pHead1.val <= pHead2.val:
                node.next = pHead1
                pHead1 = pHead1.next
            else:
                node.next = pHead2
                pHead2 = pHead2.next
            node = node.next
        if pHead1 is None:
            node.next = pHead2
        elif pHead2 is None:
            node.next = pHead1
        return dummy.next
