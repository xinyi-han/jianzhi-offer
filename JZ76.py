class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param pHead ListNode类
# @return ListNode类
#
class Solution:
    def deleteDuplication(self, pHead: ListNode) -> ListNode:
        stack = list()
        while pHead is not None:
            flag = False
            while len(stack) > 0 and pHead.val == stack[-1].val:
                flag = True
                pHead = pHead.next
                if pHead is None:
                    break
            if flag:
                stack.pop()
            else:
                stack.append(pHead)
                pHead = pHead.next
        prev = None
        for node in stack[::-1]:
            node.next = prev
            prev = node
        return prev
