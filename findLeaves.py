# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        Lists=[]

    def DFS_post_order(self,node,level):
        left_level=self.DFS_post_order(node.left,level)
        cur_level=max(left_level,right_level)+1
