from typing import List


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
# @return int整型一维数组
#
class Solution:
    def PrintFromTopToBottom(self, root: TreeNode) -> List[int]:
        output = list()
        queue = list()
        queue.append(root)
        while len(queue) > 0:
            vals = list()
            level = list()
            for node in queue:
                if node is None:
                    continue
                vals.append(node.val)
                level.append(node.left)
                level.append(node.right)
            queue = level
            output.extend(vals)
        return output
