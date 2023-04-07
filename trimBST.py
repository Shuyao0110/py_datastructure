# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if root is None:
            return root
        if root.val<low:
            root=root.right
            root=self.trimBST(root,low,high)
        elif root.val>high:
            root=root.left
            root=self.trimBST(root,low,high)
        else:
            root.right=self.trimBST(root.right,low,high)
            root.left=self.trimBST(root.left,low,high)
        return root

