class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
#
# @param root TreeNode类
# @param sum int整型
# @return int整型
#
class Solution:
    def FindPath(self, root: TreeNode, sum: int) -> int:
        if root is None:
            return 0
        stack = list()
        stack.append(root)
        closeList = set()
        closeList.add(None)
        path = list()
        num = 0
        while len(stack) > 0:
            while len(path) > 0 and (path[-1].left in closeList and path[-1].right in closeList):
                vals = list(map(lambda x: x.val, path))
                prev = 0
                for val in vals[::-1]:
                    prev += val
                    if prev == sum:
                        num += 1
                path.pop()
            node = stack.pop()
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
            closeList.add(node)
            path.append(node)
        while len(path) > 0 and (path[-1].left in closeList and path[-1].right in closeList):
            vals = list(map(lambda x: x.val, path))
            prev = 0
            for val in vals[::-1]:
                prev += val
                if prev == sum:
                    num += 1
            path.pop()
        return num
