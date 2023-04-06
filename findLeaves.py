# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        # self.lists=[]
        # level=0
        # self.DFS_post_order(root,level)
        # return self.lists

    # def DFS_post_order(self,node,level):
    #     if node is None:
    #         return -1
    #     left_level=self.DFS_post_order(node.left,level)
    #     right_level=self.DFS_post_order(node.right,level)
    #     # 开始对当前节点进行操作
    #     level=max(left_level,right_level)+1
    #     if level>=len(self.lists):
    #         self.lists.append([])
    #     self.lists[level].append(node.val)
    #     return level

        self.lists=[]
        self.DFS_post_order(root,self.lists)
        return self.lists

    def DFS_post_order(self,node,lists):
        if node is None:
            return -1
        # 每次递归的返回值（当前节点高度）都被作为左右子节点被记录
        left_level=self.DFS_post_order(node.left,lists)
        right_level=self.DFS_post_order(node.right,lists)
        # 开始对当前节点进行操作
        cur_level=max(left_level,right_level)+1
        if cur_level>=len(self.lists):
            self.lists.append([])
        self.lists[cur_level].append(node.val)
        # 如果不返回cur_level，父节点的left_level和right_level将无法被赋值
        return cur_level
        