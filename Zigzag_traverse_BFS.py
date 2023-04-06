# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# BFS锯齿形锯齿形层次遍历
# 从左到右一层，从右到左一层，交替
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        lists = []
        queue = []
        if not root:
            return lists
        is_left_to_right = True
        queue.append(root)
        while len(queue) > 0:
            break_point = len(queue)
            minil = []
            for i in range(break_point):
                node = queue.pop(0)
                minil.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            if not is_left_to_right:
                minil.reverse()
            lists.append(minil)
            is_left_to_right = not is_left_to_right
        return lists
