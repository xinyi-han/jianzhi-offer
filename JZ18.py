class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param head ListNode类
# @param val int整型
# @return ListNode类
#
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None
        elif head.val == val:
            return head.next
        node = head
        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
                break
            node = node.next
        return head

# RecursionError: maximum recursion depth exceeded in comparison
# class Solution:
#     def deleteNode(self, head: ListNode, val: int) -> ListNode:
#         if head is None:
#             return None
#         if head.val == val:
#             return head.next
#         head.next = self.deleteNode(head.next, val)
#         return head
